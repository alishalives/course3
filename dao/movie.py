from dao.model.movie import Movie
from sqlalchemy import desc


class MovieDAO:
    """ Создание слоя DAO с методами обработки данных """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_movies = self.session.query(Movie).all()
        return all_movies

    def get_one(self, mid):
        movie = self.session.query(Movie).get(mid)
        return movie

    def get_by_page(self, page, status):
        if status == "new":
            page_movies = self.session.query(Movie).order_by(desc(Movie.year)).limit(12 * page)
        else:
            page_movies = self.session.query(Movie).limit(12 * page)
        return page_movies
