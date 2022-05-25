import unittest
from http import HTTPStatus
from unittest import mock

import pytest

from src.models import User
from src.models.photo import Photo


@pytest.mark.usefixtures('client')
class ApproveViewTest(unittest.TestCase):
    def setUp(self):
        self.photo_not_approved_id = Photo.insert_one(url='url', author='tres', is_approved=False)
        self.user_id = User.insert_one(name='jaspion', password='jaspion123')
        self.user_id_superuser = User.insert_one(name='poweRangeRosa',
                                                 password='poweRangeRosa123',
                                                 is_superuser=True)

    def tearDown(self):
        Photo.delete_one(self.photo_not_approved_id)
        User.delete_one(self.user_id)
        User.delete_one(self.user_id_superuser)

    @mock.patch('src.services.user_service.UserService.get_user_by_id')
    @mock.patch('src.services.auth_service.AuthService.user_id_from_token')
    @mock.patch('src.services.auth_service.AuthService.make_token')
    def test_when_superuser_approves_a_photo_then_msg_ok(self, mock_token, mock_user_id, mock_user):
        # Arrange
        photo_before = Photo.find_one(_id=self.photo_not_approved_id)
        mock_token.return_value = 'token'
        mock_user_id.return_value = 'token'
        mock_user.return_value = User.find_one(_id=self.user_id_superuser)
        expected = HTTPStatus.OK

        # Act
        response = self.client.put(f'/photos/{self.photo_not_approved_id}/approve/',
                                   headers={'Authorization': 'token'})

        # Assert
        self.assertEqual(expected, response.status_code)
        photo = Photo.find_one(_id=self.photo_not_approved_id)
        self.assertFalse(photo_before.is_approved)
        self.assertTrue(photo.is_approved)

    # @mock.patch('src.services.auth_service.AuthService.make_token')
    # def test_when_user_approves_photo_who_not_exists_then_bad_request(self, mock_token):
    #     # Arrange
    #     photo_id_not_exists = '7384279479794937'
    #     mock_token.return_value = 'token'
    #
    #     expected = HTTPStatus.BAD_REQUEST
    #
    #     # Act
    #     response = self.client.put(f'/photos/{photo_id_not_exists}/approve/',
    #                                headers={'Authorization': 'token'})
    #
    #     # Assert
    #     self.assertEqual(expected, response.status_code)
    #
    # @mock.patch('src.services.auth_service.AuthService.make_token')
    # def test_when_user_is_not_authenticated_then_unauthorized(self, mock_token):
    #     # Arrange
    #
    #     mock_token.return_value = 'token'
    #
    #     expected = HTTPStatus.UNAUTHORIZED
    #
    #     # Act
    #     response = self.client.put(f'/photos/{self.photo_not_approved_id}/approve/',
    #                                headers={'Authorization': 'not_token'})
    #
    #     # Assert
    #     self.assertEqual(expected, response.status_code)

