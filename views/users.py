from dao.model.user import UserSchema
from flask_restx import Namespace, Resource
from implemented import user_service

user_ns = Namespace("users")


@user_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        return UserSchema(many=True).dump(user_service.get_all()), 200


@user_ns.route("/<int:uid>")
class DirectorView(Resource):
    def get(self, uid):
        return UserSchema().dump(user_service.get_one(uid)), 200
