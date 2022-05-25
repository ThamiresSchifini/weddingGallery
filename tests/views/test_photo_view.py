import unittest
from http import HTTPStatus

import bson
import pytest

from src.models.photo import Photo


@pytest.mark.usefixtures('client')
class PhotoViewTest(unittest.TestCase):
    def setUp(self):
        url = 'url'
        self.photo_1_id = Photo.insert_one(url=url, author='um', is_approved=True)
        self.photo_2_id = Photo.insert_one(url=url, author='dois', is_approved=True)
        self.photo_not_approved_id = Photo.insert_one(url=url, author='tres', is_approved=False)

        self.created_photos_id = []

    def tearDown(self):
        Photo.delete_one(self.photo_1_id)
        Photo.delete_one(self.photo_2_id)
        Photo.delete_one(self.photo_not_approved_id)

        for id_ in self.created_photos_id:
            Photo.delete_one(bson.ObjectId(id_))

    def test_when_get_photos_then_success(self):
        # Arrange
        expected_code = HTTPStatus.OK

        # Act
        actual_result = self.client.get('/photos/')

        # Assert
        self.assertEqual(expected_code, actual_result.status_code)

    def test_when_get_photos_then_approved_photos_returned(self):
        # Arrange
        expected_photo_count = 2

        # Act
        actual_result = self.client.get('/photos/')

        # Assert
        actual_photo_count = len(actual_result.json)
        self.assertEqual(actual_photo_count, expected_photo_count)

    def test_when_user_post_photo_with_success(self):
        # Arrange
        description = ''
        url = 'mock.com'
        author = 'thamires'

        # Act
        response = self.client.post('/photos/', json={
            'description': description,
            'url': url,
            'author': author
        })
        self.created_photos_id.append(response.json['_id'])

        # Assert
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.json['description'], description)
        self.assertEqual(response.json['url'], url)
        self.assertEqual(response.json['author'], author)


    #
    # # Arrange
    #
    # # Act
    #
    # # Assert
    #
    # def test_foo_with_client(self):
    #     expected_result = {}
    #
    #     actual_result = self.client.get('/hello')
    #
    #     self.assertEqual(actual_result, expected_result)

    # def test_bar_with_client(self):
    #     # Use the client here
    #     # Example login request (on a hypothetical app)
    #     rv = self.client.post('/login', {'username': 'pinkerton', 'password': 'secret_key'})
    #     # Make sure rv is a redirect request to index page
    #     self.assertLocationHeader('http://localhost/')
    #     # Make sure session is set
    #     self.assertIn('user_id', flask.globals.session)
