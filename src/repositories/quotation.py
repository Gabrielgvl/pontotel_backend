""" Defines the Quotation repository """
from config import ALPHAVANTAGE_API_KEY
from alpha_vantage.timeseries import TimeSeries


class QuotationRepository:
    """ The repository for the quotation model """

    @staticmethod
    def get_bovespa():
        """ Query a quotation by last and first name """
        ts = TimeSeries(key=ALPHAVANTAGE_API_KEY)
        data, meta_data = ts.get_daily(symbol='IBM')
        return data
