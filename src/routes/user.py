"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import LoginResource, RegisterResource

USER_BLUEPRINT = Blueprint("user", __name__)
Api(USER_BLUEPRINT).add_resource(
    LoginResource, "/login"
)

Api(USER_BLUEPRINT).add_resource(
    RegisterResource, "/register"
)