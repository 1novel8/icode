from src.models.contract import Contract
from src.models.project import Project
from src.repositories.base import BaseRepository


class ProjectRepository(BaseRepository):
    model = Project

    def add_contract(self, contract: Contract, project: Project):
        project.contracts.append(contract)

    def active_contracts_count(self, project):
        count = self.session.query(Contract).filter(
            Contract.status == 'ACTIVE', Contract.project == project
        ).count()
        return count

