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
    options = db.Column(db.JSON)

    def __init__(self, username, hashed_password, options=None):
        """ Create a new User """
        if options is None:
            options = {}
        self.options = options
        self.hashed_password = hashed_password
        self.username = username
