"""
Define the REST verbs relative to the quotations
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from repositories import QuotationRepository


class QuotationResource(Resource):
    """ Verbs relative to the quotations """

    @staticmethod
    @swag_from("../swagger/quotation/GET.yml")
    @jwt_required
    def get(company_symbol):
        """ Return an quotation key information based on his name """
        if company_symbol == 'bovespa':
            quotation = QuotationRepository.get_bovespa()
        else:
            quotation = QuotationRepository.get_company(company_symbol)
        return jsonify({company_symbol: quotation})
