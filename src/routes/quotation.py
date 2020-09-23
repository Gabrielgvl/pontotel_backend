"""
Defines the blueprint for the quotations
"""
from flask import Blueprint
from flask_restful import Api

from resources import QuotationResource

QUOTATION_BLUEPRINT = Blueprint("quotation", __name__)
Api(QUOTATION_BLUEPRINT).add_resource(
    QuotationResource, "/quotation"
)
