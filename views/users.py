from flask import request, abort
from dao.model.user import UserSchema
from flask_restx import Namespace, Resource

from helpers.decorators import auth_required
from implemented import user_service

user_ns = Namespace("users")


@user_ns.route("/")
class UsersView(Resource):
    @auth_required
    def get(self):
        users = user_service.get_all()

        user_list = []

        for user in users:
            data = {
                "id": user.id,
                "email": user.email,
                "surname": user.surname,
                "name": user.name
            }
            user_list.append(data)
        return UserSchema(many=True).dump(user_list), 200


@user_ns.route("/<int:uid>")
class UserView(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_one(uid)

        data = {
            "id": user.id,
            "email": user.email,
            "surname": user.surname,
            "name": user.name
        }
        return UserSchema().dump(data), 200

    @auth_required
    def patch(self, uid):
        req_json = request.json
        req_json["id"] = uid
        try:
            user = user_service.update_partial(req_json)
            return "", 204
        except Exception as e:
            return e


@user_ns.route("/password")
class UserView(Resource):
    @auth_required
    def put(self):
        req_json = request.json

        email = req_json.get("email", None)
        now_password = req_json.get("now_password", None)
        new_password = req_json.get("new_password", None)
        if None in [email, now_password, new_password]:
            abort(401)

        user = user_service.get_by_email(email)

        if user is None:
            return {"error": "Неверные учётные данные"}, 401
        elif not user_service.compare_passwords(user.password, now_password):
            return {"error": "Неверные учётные данные"}, 401

        user = user_service.update_password(email, new_password)
        return "", 204

