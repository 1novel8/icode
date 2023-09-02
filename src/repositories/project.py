from src.models.contract import Contract
from src.models.project import Project
from src.repositories.base import BaseRepository


class ProjectRepository(BaseRepository):
    model = Project

    def add_contract(self, contract: Contract, project: Project):
        project.contracts.append(contract)

    def list(self) -> list:
        projects = self.session.query(self.model).all()
        return projects