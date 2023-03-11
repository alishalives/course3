from dao.model.director import Director


class DirectorDAO:
    """ Создание слоя DAO с методами обработки данных """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_director = self.session.query(Director).all()
        return all_director

    def get_one(self, did):
        director = self.session.query(Director).get(did)
        return director
