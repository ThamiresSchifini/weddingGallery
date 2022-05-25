from flask import Blueprint

from src.views import PhotoView, LoginView, ApproveView, ReactionView

photos_blueprint = Blueprint('photos', __name__, url_prefix='/photos')
photos_blueprint.route('/', methods=('GET', 'POST'))(PhotoView.as_view('photos'))
photos_blueprint.route('/<photo_id>/approve/', methods=('PUT',))(ApproveView.as_view('approve'))
photos_blueprint.route('/<photo_id>/reactions/', methods=('PUT',))(ReactionView.as_view('reactions'))

users_blueprint = Blueprint('users', __name__, url_prefix='/users')
users_blueprint.route('/login/', methods=('POST',))(LoginView.as_view('login'))

