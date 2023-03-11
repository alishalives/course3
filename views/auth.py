from dao.model.user import UserSchema
from flask_restx import Namespace, Resource
from implemented import auth_service
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

        return auth_service.is_check(email, password)




