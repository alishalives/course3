from marshmallow import Schema, fields
from setup_db import db


class User(db.Model):
    """ Создание модели таблицы user с необходимыми полями"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, nullable=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = (db.Integer, db.ForeignKey("genre.id"))
    # genre = db.relationship("Genre")


class UserSchema(Schema):
    """ Создание схемы таблицы user для дальнейшей сериализации """
    id = fields.Int()
    email = fields.Email()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Int()
