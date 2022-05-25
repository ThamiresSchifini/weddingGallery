from typing import List

from src.models import MongoDocument


class User(MongoDocument):
    """ """
    def __init__(self, document):
        super().__init__(document)

        self.name: str = document.get('name')
        self.password: str = document.get('password')
        self.is_superuser: bool = document.get('is_superuser', False)


    class Meta:
        collection = 'users'

    def serialize(self):
        return dict(
            _id=self._id,
            name=self.name,
            is_superuser=self.is_superuser,
        )
