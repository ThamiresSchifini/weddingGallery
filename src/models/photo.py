from typing import List

from src.models import MongoDocument


class Photo(MongoDocument):
    """ """
    def __init__(self, document):
        super().__init__(document)

        self.description: str = document.get('description')
        self.likes: int = document.get('likes', 0)
        self.comments: List[str] = document.get('comments', [])
        self.url: str = document.get('url')
        self.author: str = document.get('author')
        self.is_approved: bool = document.get('is_approved', False)

    class Meta:
        collection = 'photos'

    def serialize(self):
        return dict(
            _id=self._id,
            description=self.description,
            likes=self.likes,
            comments=self.comments,
            url=self.url,
            author=self.author,
            is_approved=self.is_approved,
        )
