"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Quotation(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "quotation"

    symbol = db.Column(db.String(10), primary_key=True)
    data = db.Column(db.JSON)
    date = db.Column(db.Date(), )
    open = db.Column(db.Float(4))
    high = db.Column(db.Float(4))
    low = db.Column(db.Float(4))
    volume = db.Column(db.Float(4))
    price = db.Column(db.Float(4), nullable=True)
    latest_trading_day = db.Column(db.Date(), nullable=True)
    previous_close = db.Column(db.Float(4), nullable=True)
    change = db.Column(db.Float(4), nullable=True)
    change_percent = db.Column(db.Float(4), nullable=True)

    def __init__(self, symbol, open, high, low, price, volume, latest_trading_day, previous_close, change,
                 change_percent):
        """ Create a new Quotation """
        self.price = price
        self.volume = volume
        self.latest_trading_day = latest_trading_day
        self.previous_close = previous_close
        self.low = low
        self.change = change
        self.high = high
        self.change_percent = change_percent
        self.open = open
        self.symbol = symbol
