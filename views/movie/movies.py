from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        # Принимаем данные для фильтров
        data_filter = request.args
        all_movies = movie_service.get_all(data_filter)

        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return [], 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception:
            return '', 404

    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid
        movie_service.update(req_json)
        return [], 204

    def patch(self, mid):
        req_json = request.json
        req_json['id'] = mid
        movie_service.update_partial(req_json)
        return [], 204

    def delete(self, mid):
        movie_service.delete(mid)

        return [], 204
