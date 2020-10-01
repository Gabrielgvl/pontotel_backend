"""
Define the REST verbs relative to the quotations
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from repositories import CompanyRepository


class CompanyResource(Resource):
    """ Verbs relative to the quotations """

    @staticmethod
    @swag_from("../swagger/company/GET.yml")
    @jwt_required
    def get():
        return {"companies": CompanyRepository.get()}
