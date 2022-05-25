import bson

from src.models import Photo


class PhotoService:
    @staticmethod
    def get_photo_by_id(_id: str):
        mongo_id = bson.ObjectId(_id)
        return Photo.find_one(_id=mongo_id)

    @staticmethod
    def increment_likes(photo: Photo):
        mongo_id = bson.ObjectId(photo._id)
        return Photo.update_one({'_id': mongo_id}, {'$inc': {'likes': 1}})

    @staticmethod
    def add_comment(photo: Photo, comment: str):
        mongo_id = bson.ObjectId(photo._id)
        return Photo.update_one({'_id': mongo_id}, {'$push': {'comments': comment}})

    @staticmethod
    def approve_photo(photo: Photo, is_approved: bool):
        mongo_id = bson.ObjectId(photo._id)
        if is_approved:
            return Photo.update_one({'_id': mongo_id}, {'$set': {'is_approved': True}})
        else:
            return Photo.delete_one(mongo_id)
