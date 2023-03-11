from dao.model.director import DirectorSchema
from flask_restx import Namespace, Resource
from implemented import director_service

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        return DirectorSchema(many=True).dump(director_service.get_all()), 200


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        return DirectorSchema().dump(director_service.get_one(did)), 200

