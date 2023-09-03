from sqlalchemy.orm import Session

from src.exceptions import NotFoundException, NoSessionException


class BaseRepository:
    model = None

    def __init__(self, **kwargs):
        try:
            self.session = kwargs.get('session')
            if not isinstance(self.session, Session):
                raise NoSessionException
        except NoSessionException:
            print('!!!Вы не передали сессию в репозиторий!!!')
            exit()

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

