"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    hashed_password = db.Column(db.String(500))

    def __init__(self, username, hashed_password, id=None):
        """ Create a new User """
        self.id = id
        self.hashed_password = hashed_password
        self.username = username


class UserOptions(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User Options model """

    __tablename__ = "user_options"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User")
    username = db.Column(db.String(20))
    hashed_password = db.Column(db.String(500))

    def __init__(self, username, hashed_password, id=None):
        """ Create a new User """
        self.id = id
        self.hashed_password = hashed_password
        self.username = username
