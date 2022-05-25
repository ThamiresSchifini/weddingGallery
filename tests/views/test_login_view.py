import unittest
from http import HTTPStatus
from unittest import mock

import pytest

from src.models import User
from src.models.photo import Photo


@pytest.mark.usefixtures('client')
class PhotoViewTest(unittest.TestCase):
    def setUp(self):
        url = 'url'
        self.photo_1_id = Photo.insert_one(url=url, author='um', is_approved=True)
        self.photo_2_id = Photo.insert_one(url=url, author='dois', is_approved=True)
        self.photo_not_approved_id = Photo.insert_one(url=url, author='tres', is_approved=False)
        self.user_id = User.insert_one(name='jaspion', password='jaspion123')
        self.user_id_superuser = User.insert_one(name='poweRangeRosa',
                                                 password='poweRangeRosa123',
                                                 is_superuser=True)

    def tearDown(self):
        Photo.delete_one(self.photo_1_id)
        Photo.delete_one(self.photo_2_id)
        Photo.delete_one(self.photo_not_approved_id)
        User.delete_one(self.user_id)
        User.delete_one(self.user_id_superuser)

    @mock.patch('src.services.auth_service.AuthService.make_token')
    @mock.patch('src.services.auth_service.AuthService.check_password')
    def test_when_user_login_with_success_then_token(self, mock_password, mock_token):
        # Arrange
        mock_password.return_value = True
        mock_token.return_value = 'token'

        data = {
            'name': 'jaspion',
            'password': 'jaspion123'
        }
        expected = {'token': 'token'}

        # Act
        response = self.client.post('/users/login/', json=data)

        # Assert
        self.assertEqual(expected, response.json)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_when_user_login_not_exist_then_bad_request(self):
        # Arrange
        data = {
            'name': 'Naruto',
            'password': 'Naruto123'
        }
        expected = HTTPStatus.BAD_REQUEST

        # Act
        response = self.client.post('/users/login/', json=data)

        # Assert
        self.assertEqual(expected, response.status_code)

    @mock.patch('src.services.auth_service.AuthService.check_password')
    def test_when_user_login_with_wrong_password_then_bad_request(self, mock_password):
        # Arrange
        mock_password.return_value = False
        data = {
            'name': 'jaspion',
            'password': 'jaspion12'
        }
        expected = HTTPStatus.BAD_REQUEST

        # Act
        response = self.client.post('/users/login/', json=data)

        # Assert
        self.assertEqual(expected, response.status_code)

    def test_when_user_login_without_password_then_bad_request(self):
        # Arrange
        data = {
            'name': 'jaspion',
        }
        expected = HTTPStatus.BAD_REQUEST

        # Act
        response = self.client.post('/users/login/', json=data)

        # Assert
        self.assertEqual(expected, response.status_code)

