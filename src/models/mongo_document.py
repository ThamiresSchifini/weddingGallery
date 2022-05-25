from bson import ObjectId
from decouple import config
from flask import g
import pymongo


class MongoDocument:
    """Should be used as:

    class Model(MongoDocument):
        class Meta:
            collection = 'my-collection'
    """
    def __init__(self, document):
        self._id = str(document['_id'])

    @staticmethod
    def __client() -> pymongo.MongoClient:
        return g.mongo_client

    @staticmethod
    def __db():
        return MongoDocument.__client().gallery if config('IS_PRODUCTION', False) \
            else MongoDocument.__client().test_gallery

    class Meta:
        collection = None

    @classmethod
    def collection(cls):
        collection_name = cls.Meta.collection
        if collection_name is None:
            raise ValueError(f'Collection not defined for {cls.__qualname__}')

        return MongoDocument.__db()[collection_name]

    @classmethod
    def find_one(cls, **kwargs):
        instance = cls.collection().find_one(kwargs)
        if instance is None:
            return None

        return cls(instance)

    @classmethod
    def find(cls, **kwargs):
        return (cls(doc) for doc in cls.collection().find(kwargs))

    @classmethod
    def count(cls, **kwargs):
        return cls.collection().count_documents(kwargs)

    @classmethod
    def insert_one(cls, **kwargs) -> ObjectId:
        return cls.collection().insert_one(kwargs).inserted_id

    @classmethod
    def delete_one(cls, _id: ObjectId):
        cls.collection().delete_one(dict(_id=_id))

    @classmethod
    def delete_many(cls, **kwargs):
        return cls.collection().delete_many(kwargs)

    @classmethod
    def update_one(cls, filter_, operations):
        return cls.collection().update_one(filter_, operations).modified_count
