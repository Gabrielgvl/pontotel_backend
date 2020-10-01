"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Quotation(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "quotation"
    __table_args__ = (db.UniqueConstraint('company_id', 'date', name='_company_date_uc'),)

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    date = db.Column(db.Date)
    data = db.Column(db.JSON)
    # company = db.relationship("Company", back_populates="quotations")

    def __init__(self, company_id, date, data):
        """ Create a new Quotation """
        self.date = date
        self.company_id = company_id
        self.data = data
