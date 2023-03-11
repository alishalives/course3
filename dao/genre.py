from dao.model.genre import Genre


class GenreDAO:
    """ Создание слоя DAO с методами обработки данных """

    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_genres = self.session.query(Genre).all()
        return all_genres

    def get_one(self, gid):
        genre = self.session.query(Genre).get(gid)
        return genre
