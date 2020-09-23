"""
Define the REST verbs relative to the quotations
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource

from repositories import  QuotationRepository


class QuotationResource(Resource):
    """ Verbs relative to the quotations """

    @staticmethod
    @swag_from("../swagger/quotation/GET.yml")
    def get():
        """ Return an quotation key information based on his name """
        quotation = QuotationRepository.get_bovespa()
        return jsonify({"bovespa": quotation.json})

