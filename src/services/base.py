
class BaseService:
    repo = None

    def __init__(self, **kwargs):
        self.repository = self.repo(session=kwargs.get('session'))

    def create(self, name: str):
        return self.repository.create(name=name)

    def get_by_id(self, pk: int):
        return self.repository.get_by_id(pk=pk)

    def list(self) -> list:
        return self.repository.list()
