"""
Define the REST verbs relative to the users
"""
import base64
from flask import request
from flasgger import swag_from
from flask import jsonify, abort
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.orm.exc import NoResultFound

from repositories import UserRepository
from util import parse_params


class LoginResource(Resource):
    """ Verbs relative to the users login"""

    @staticmethod
    @swag_from("../swagger/user/LOGIN.yml")
    def get():
        """ Return an user key information based on his name """
        if 'Authorization' not in request.headers:
            return abort(403, description='Authorization header is missing!')
        authorization = request.headers['Authorization']
        _, enconded_auth = authorization.split(' ')
        username, hashed_password = base64.b64decode(enconded_auth).decode("utf-8").split(':')
        try:
            user = UserRepository.get(username=username, hashed_password=hashed_password)
        except NoResultFound:
            abort(403, "Usuário não encontrado!")

        if not user:
            return abort(403, description='Username or Password are incorrect!')

        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token})


class RegisterResource(Resource):
    """ Verbs relative to the users register"""

    @staticmethod
    @parse_params(
        Argument("username", location="json", required=True, help="The username of the user."),
        Argument("hashed_password", location="json", required=True, help="The hashed_password of the user.")
    )
    @swag_from("../swagger/user/REGISTER.yml")
    def post(username, hashed_password):
        """ Create an user based on the sent information """
        try:
            user = UserRepository.create(username=username, hashed_password=hashed_password)
            access_token = create_access_token(identity=username)
            return jsonify({"access_token": access_token})
        except:
            return abort(403, description="Username already exists!")


class UpdateOptionsResource(Resource):
    """ Verbs relative to the users options"""

    @staticmethod
    @parse_params(
        Argument("options", location="json", required=True, help="The username of the user."),
    )
    @swag_from("../swagger/user/REGISTER.yml")
    def post(user_id, options):
        """ Create an user based on the sent information """
        try:
            user = UserRepository.get_by_id(user_id)
            user.options = options
            user.save()
            return user.json
        except:
            return abort(404, description="User doesn't exist!")
