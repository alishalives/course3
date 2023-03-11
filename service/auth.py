import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.auth import AuthDAO


class AuthService:
    def __init__(self, dao: AuthDAO):
        self.dao = dao

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    def compare_passwords(self, hash_password, user_password):
        user_password_to_hash = hashlib.pbkdf2_hmac(
            'sha256',
            user_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
        return hmac.compare_digest(hash_password, user_password_to_hash)

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def is_check(self, email, password):
        if self.compare_passwords(self.dao.is_check(email), password):
            return True
        else:
            return False
