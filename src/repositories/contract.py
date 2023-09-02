from src.enums import Status
from src.models.contract import Contract
from src.repositories.base import BaseRepository


class ContractRepository(BaseRepository):
    model = Contract

    def active_count(self, **kwargs):
        query = self.session.query(self.model)
        if kwargs.get('project_id'):
            query = query.filter(self.model.project_id == kwargs.get('project_id'))
        return query.count()

    def set_status(self, contract: Contract, status: Status):
        contract.status = status

    def projects_list(self, project_id: int):
        return (self.session.query(self.model).
                filter(self.model.project_id == project_id))

    def list(self, **kwargs) -> list:
        query = self.session.query(self.model)
        if kwargs.get('project_id'):
            query = query.filter(self.model.project_id == kwargs.get('project_id'))
        return query
