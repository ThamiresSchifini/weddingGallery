from decouple import config
from flask import Flask, g, request
from pymongo import MongoClient

from src.blueprints import photos_blueprint, users_blueprint
from src.services import UserService, AuthService


def inject_user_from_token():
    token = request.headers.get('Authorization')
    if token is None or token == '':
        return

    id_from_token = AuthService.user_id_from_token(token)

    user = UserService.get_user_by_id(id_from_token)
    if user is None:
        return

    g.user = user


def create_app(**kwargs):
    app = Flask(__name__)

    # app.config['CORS_HEADERS'] = 'Content-Type'

    app.register_blueprint(photos_blueprint)
    app.register_blueprint(users_blueprint)

    mongo_host = config('MONGO_HOST', kwargs.get('MONGO_HOST'))
    client = MongoClient(
        mongo_host
    )

    @app.before_request
    def before_request():
        g.mongo_client = client
        inject_user_from_token()

    @app.after_request
    def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        header['Access-Control-Allow-Headers'] = '*'  # ['Authorization']
        header['Access-Control-Allow-Methods'] = '*'
        return response

    return app


if __name__ == '__main__':
    app_ = create_app()

    app_.run()
