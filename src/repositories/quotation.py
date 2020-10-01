""" Defines the Quotation repository """
from sqlalchemy.orm.exc import NoResultFound

from config import ALPHAVANTAGE_API_KEY
from alpha_vantage.timeseries import TimeSeries

from models import Company, Quotation
from util.quotation_utils import map_quotation_key


class QuotationRepository:
    """ The repository for the quotation model """

    @staticmethod
    def get(company_id, date):
        try:
            return Quotation.query.filter_by(company_id=company_id, date=date).one()
        except NoResultFound:
            return None


    @staticmethod
    def get_bovespa():
        """ Query bovespa values """
        ts = TimeSeries(key=ALPHAVANTAGE_API_KEY)
        data, meta_data = ts.get_quote_endpoint(symbol='PETR4.SAO')
        return map_quotation_key(data)

    @classmethod
    def get_company(cls, company_symbol):
        """ Query a company by its symbol """
        company = Company.query.filter_by(symbol=company_symbol).one()
        fetch_full = len(company.quotations) == 0

        try:
            ts = TimeSeries(key=ALPHAVANTAGE_API_KEY)
            data, meta_data = ts.get_daily_adjusted(symbol=company_symbol, outputsize=fetch_full)
            for date, quotation_data in data.items():
                mapped_qd = map_quotation_key(quotation_data)
                data[date] = mapped_qd
                quotation = cls.get(company_id=company.id, date=date)
                if quotation:
                    quotation.data = mapped_qd
                    quotation.save()
                else:
                    Quotation(company_id=company.id, date=date, data=mapped_qd).save()

            return data
        except ValueError:
            return Quotation.query.filter_by(company_id=company.id).all()


