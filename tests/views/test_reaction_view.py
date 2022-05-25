import unittest
from http import HTTPStatus
from unittest import mock

import pytest

from src.models import User
from src.models.photo import Photo


@pytest.mark.usefixtures('client')
class ReactionViewTest(unittest.TestCase):
    def setUp(self):
        self.photo_1_id = Photo.insert_one(url='url', author='um', is_approved=True, comments=[], likes=0)

    def tearDown(self):
        Photo.delete_one(self.photo_1_id)

    def test_when_user_comment_photo_then_status_code_ok(self):
        # Arrange
        data = {
            'comment': 'Awesome',
        }
        expected = HTTPStatus.OK

        # Act
        response = self.client.put(f'/photos/{self.photo_1_id}/reactions/', json=data)

        # Assert
        self.assertEqual(expected, response.status_code)
        photo = Photo.find_one(_id=self.photo_1_id)
        self.assertIn('Awesome', photo.comments)

    def test_when_user_liked_photo_then_status_code_ok(self):
        # Arrange
        data = {
            'like': True,
        }
        expected = HTTPStatus.OK
        expected_likes = 1

        # Act
        response = self.client.put(f'/photos/{self.photo_1_id}/reactions/', json=data)

        # Assert
        self.assertEqual(expected, response.status_code)
        photo = Photo.find_one(_id=self.photo_1_id)
        self.assertEqual(expected_likes, photo.likes)
