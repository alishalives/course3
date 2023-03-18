from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_hash(self, password):
        return self.dao.get_hash(password)

    def compare_passwords(self, hash_password, user_password):
        return self.dao.compare_passwords(hash_password, user_password)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def update_password(self, email, new_password):
        return self.dao.update_password(email, new_password)

    def update_partial(self, data):
        return self.dao.update_partial(data)
