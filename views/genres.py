from dao.model.genre import GenreSchema
from flask_restx import Namespace, Resource
from implemented import genre_service

genre_ns = Namespace("genres")


@genre_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        return GenreSchema(many=True).dump(genre_service.get_all()), 200


@genre_ns.route("/<int:gid>")
class DirectorView(Resource):
    def get(self, gid):
        return GenreSchema().dump(genre_service.get_one(gid)), 200
