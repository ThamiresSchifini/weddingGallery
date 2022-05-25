from http import HTTPStatus

from flask import make_response, request
from flask.views import MethodView

from src.services import PhotoService
from src.utils.decorators import superuser_required


class ApproveView(MethodView):
    decorators = [superuser_required]

    def put(self, *_args, **_kwargs):
        photo_id = request.view_args.get('photo_id')
        data = request.json
        if data.get('approve') is None:
            return make_response({'message': 'needs approve value'}, HTTPStatus.BAD_REQUEST)

        photo = PhotoService.get_photo_by_id(photo_id)
        if photo is None:
            return make_response({'message': 'photo not found'}, HTTPStatus.BAD_REQUEST)

        PhotoService.approve_photo(photo, data['approve'])
        return make_response({'message': 'ok'}, HTTPStatus.OK)
