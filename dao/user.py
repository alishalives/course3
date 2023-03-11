from dao.model.user import User


class UserDAO:
    """ Создание слоя DAO с методами обработки данных """

    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_users = self.session.query(User).all()
        return all_users

    def get_one(self, uid):
        user = self.session.query(User).get(uid)
        return user
    