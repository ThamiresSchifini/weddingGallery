from http import HTTPStatus

from flask import g, make_response


def superuser_required(f):
    """Checks whether the logged user is superuser."""

    def decorator(*args, **kwargs):
        if not g.get('user'):
            return make_response({'message': 'superuser needs to be authenticated'}, HTTPStatus.UNAUTHORIZED)

        if not g.user.is_superuser:
            return make_response({'message': 'user authenticated is not a superuser'}, HTTPStatus.UNAUTHORIZED)

        return f(*args, **kwargs)

    return decorator
