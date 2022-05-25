import bson

from src.models import User


class UserService:
    @staticmethod
    def get_user_by_id(_id: str):
        mongo_id = bson.ObjectId(_id)
        return User .find_one(_id=mongo_id)
