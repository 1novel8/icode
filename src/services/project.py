from src.models.contract import Contract
from src.models.project import Project
from src.repositories.project import ProjectRepository
from src.services.base import BaseService


class ProjectService(BaseService):
    repo = ProjectRepository

    def add_contract(self, contract: Contract, project: Project):
        self.repository.add_contract(contract=contract, project=project)

    def active_contracts_count(self, project):
        return self.repository.active_contracts_count(project=project)

    def print_projects(self) -> None:
        projects = self.list()
        print(f'Список проектов\nid\t\t name\t\t created at')
        for project in projects:
            print(f'{project.id}\t\t {project.name}\t\t {project.created_at}')
