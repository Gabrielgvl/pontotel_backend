"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Company(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Company model """

    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    symbol = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(20))
    quotations = db.relationship("Quotation", lazy=True)

    def __init__(self, symbol, name):
        """ Create a new Company """
        self.symbol = symbol
        self.name = name
