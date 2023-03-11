from dao.model.user import User


class AuthDAO:
    """ Создание слоя DAO с методами обработки данных """
    def __init__(self, session):
        self.session = session

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def is_check(self, email):
        try:
            user = self.session.query(User).filter(User.email == email).one()
            return user.password
        except Exception as e:
            return e
