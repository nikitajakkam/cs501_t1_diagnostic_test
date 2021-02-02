# project/server/users/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class GetAllUsers(MethodView):
    """
    Access all registered users
    """

    def get(self):
        listofusers = []
        users = User.query.all()
        for user in users:
            listofusers.append(user.email)
            print(user.email)
        return jsonify(listofusers), 201

# define the API resources
allusers_view = GetAllUsers.as_view('allusers_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=allusers_view,
    methods=['GET']
)