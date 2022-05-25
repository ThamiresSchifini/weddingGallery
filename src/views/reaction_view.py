from http import HTTPStatus

from flask import make_response, request
from flask.views import MethodView

from src.services import PhotoService


class ReactionView(MethodView):

    def put(self, *_args, **_kwargs):
        request_body = request.json
        photo_id = request.view_args.get('photo_id')

        photo = PhotoService.get_photo_by_id(photo_id)
        if photo is None:
            return make_response({'message': 'photo not found'}, HTTPStatus.BAD_REQUEST)

        if request_body.get('like', False):
            PhotoService.increment_likes(photo)
            return make_response({'message': 'ok'}, HTTPStatus.OK)

        if comment := request_body.get('comment'):
            PhotoService.add_comment(photo, comment)
            return make_response({'message': 'ok'}, HTTPStatus.OK)
