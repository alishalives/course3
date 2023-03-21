import calendar
import datetime

import jwt

from constants import SECRET, ALGO
from flask_restx import Namespace, Resource
from implemented import auth_service, user_service
from flask import request, abort

auth_ns = Namespace("auth")


@auth_ns.route("/register")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in [email, password]:
            abort(401)
        register_user = auth_service.create(req_json)
        return "", 201, {"location": f"/users/{register_user.id}"}


@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in [email, password]:
            abort(401)

        user = user_service.get_by_email(email)

        if user is None:
            return {"error": "Неверные учётные данные"}, 401
        elif not auth_service.is_check(email, password):
            return {"error": "Неверные учётные данные"}, 401

        data = {
            "email": user.email
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token", None)
        if refresh_token is None:
            abort(400)

        try:
            data_refresh = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=[ALGO])
            # data_access = jwt.decode(jwt=access_token, key=SECRET, algorithms=[ALGO])

            email = data_refresh.get("email")
            user = user_service.get_by_email(email)

            data = {
                "email": user.email
            }
            min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            data["exp"] = calendar.timegm(min30.timetuple())
            access_token = jwt.encode(data, SECRET, algorithm=ALGO)

            days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
            data["exp"] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

            tokens = {"access_token": access_token, "refresh_token": refresh_token}

            return tokens, 201
        except Exception as e:
            abort(400)
