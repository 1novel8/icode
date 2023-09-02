from src.models.project import Project


class BaseRepository:
    model = None

    def __init__(self, **kwargs):
        self.session = kwargs.get('session')

    def get_by_id(self, pk: int):
        return self.session.query(self.model).get(pk)

    def create(self, **kwargs):
        obj = Project(**kwargs)
        self.session.add(obj)
        self.session.commit()
        return obj

    def list(self) -> list:
        obj_list = self.session.query(self.model).all()
        return obj_list

