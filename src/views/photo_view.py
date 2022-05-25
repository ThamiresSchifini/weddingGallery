import datetime
from http import HTTPStatus

from flask import make_response, jsonify, request
from flask.views import MethodView


from src.models import Photo
from flask import g, make_response

from src.views import FileService


class PhotoView(MethodView):

    def get(self, *args, **kwargs):
        if g.get('user') and g.user.is_superuser:
            photos_list = Photo.find()
        else:
            photos_list = Photo.find(is_approved=True)
        serialized = [doc.serialize() for doc in photos_list]
        return make_response(jsonify(serialized))

    def post(self, *args, **kwargs):
        file = request.files.get('file')

        if file is None:
            return make_response({'message': 'photo file missing'}, HTTPStatus.BAD_REQUEST)

        file_url = self._upload_file_and_get_url(file)

        photo_id = Photo.insert_one(
            description=request.form.get('description'),
            url=file_url,
            author=request.form.get('author'),
        )
        photo = Photo.find_one(_id=photo_id)
        serialized = photo.serialize()
        return make_response(serialized, HTTPStatus.CREATED)

    def _upload_file_and_get_url(self, file):
        return FileService.upload_file(file)
