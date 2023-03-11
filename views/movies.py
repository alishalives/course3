from dao.model.movie import MovieSchema
from flask_restx import Namespace, Resource
from implemented import movie_service
from flask import request

movie_ns = Namespace("movies")


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        if request.args.get("page"):
            movie = movie_service.get_by_page(int(request.args.get("page")), str(request.args.get("status")))
            return MovieSchema(many=True).dump(movie), 200
        else:
            return MovieSchema(many=True).dump(movie_service.get_all()), 200


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        return MovieSchema().dump(movie_service.get_one(mid)), 200

