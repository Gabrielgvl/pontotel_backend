""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(username, hashed_password):
        """ Query a user by last and first name """
        return User.query.filter_by(username=username, hashed_password=hashed_password).one()

    @staticmethod
    def create(username, hashed_password):
        """ Create a new user """
        user = User(username=username, hashed_password=hashed_password)
        return user.save()
