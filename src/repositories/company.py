""" Defines the Quotation repository """
from sqlalchemy.orm import load_only
from sqlalchemy.orm.exc import NoResultFound


from models import Company


class CompanyRepository:
    """ The repository for the quotation model """

    @staticmethod
    def get():
        fields = ['id', 'name', 'symbol']
        try:
            companies = Company.query.options(load_only(*fields)).all()
            return [c.json for c in companies]
        except NoResultFound:
            return None
