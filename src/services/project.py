from src.enums import Status
from src.models.contract import Contract
from src.repositories.project import ProjectRepository
from src.services.base import BaseService


class ProjectService(BaseService):
    repo = ProjectRepository

    def add_contract(self, contract_id: int, project_id: int):
        pass

    def active_contracts_count(self, project):
        return self.repository.active_contracts_count(project=project)

    def print_projects(self) -> None:
        projects = self.list()
        print(f'Project list: id -- name -- created at')
        for project in projects:
            print(f'{project.id}\t {project.name}\t\t {project.created_at}')
