from src.exceptions import NotFoundException
from src.models.project import Project


class BaseRepository:
    model = None

    def __init__(self, **kwargs):
        self.session = kwargs.get('session')

    def get_by_id(self, pk: int):
        obj = self.session.query(self.model).get(pk)
        if obj is None:
            raise NotFoundException
        return obj

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        self.session.add(obj)
        self.session.commit()
        return obj

