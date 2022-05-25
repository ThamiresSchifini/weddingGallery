from http import HTTPStatus

from flask import make_response, jsonify, request
from flask.views import MethodView

from src.models import User
from src.services.auth_service import AuthService


class LoginView(MethodView):

    def post(self, *args, **kwargs):
        data = request.json
        if 'name' not in data:
            return self._make_bad_request('name is missing')
        if 'password' not in data:
            return self._make_bad_request('password is missing')

        user = User.find_one(name=data['name'])
        if user is None:
            return self._make_bad_request("user doesn't exist")

        is_correct = AuthService.check_password(user=user, password=data['password'])
        if not is_correct:
            return self._make_bad_request('password is incorrect')

        token = AuthService.make_token(user=user)
        return make_response({'name': user.name, 'token': token})


    def _make_bad_request(self, message: str):
        return make_response({'message': message}, HTTPStatus.BAD_REQUEST)
