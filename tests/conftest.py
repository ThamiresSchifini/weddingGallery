import pytest

from src.app import create_app


@pytest.fixture(scope='class')
def app(request):
    # Setup

    app = create_app(
        MONGO_USER='root',
        MONGO_PASS='Thamires',
    )

    with app.test_request_context():
        app.preprocess_request()

        request.cls.app = app

        yield app

    # Clean up


@pytest.fixture(scope='class')
def client(request, app):
    client = app.test_client()

    request.cls.client = client

    return client
