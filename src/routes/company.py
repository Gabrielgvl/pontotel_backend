"""
Defines the blueprint for the companies
"""
from flask import Blueprint
from flask_restful import Api

from resources import CompanyResource

COMPANY_BLUEPRINT = Blueprint("company", __name__)
Api(COMPANY_BLUEPRINT).add_resource(
    CompanyResource, "/company"
)
