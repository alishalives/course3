import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
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

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, hash_password, user_password):
        return hmac.compare_digest(
            base64.b64decode(hash_password),
            hashlib.pbkdf2_hmac(
                "sha256",
                user_password.encode("utf-8"),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )

    def get_by_email(self, email):
        user = self.session.query(User).filter(User.email == email).one()
        return user

    def update_password(self, email, new_password):
        user = self.get_by_email(email)
        user.password = self.get_hash(new_password)
        self.session.add(user)
        self.session.commit()
        return user

    def update_partial(self, data):
        user = self.get_one(data["id"])
        if "name" in data:
            user.name = data["name"]

        if "surname" in data:
            user.surname = data["surname"]

        if "favorite_genre" in data:
            user.favorite_genre = data["favorite_genre"]
        self.session.add(user)
        self.session.commit()
