from src.models.contract import Contract
from src.models.project import Project
from src.schemas.projects import ProjectSchema


class ProjectRepository:
    def __init__(self, **kwargs):
        self.session = kwargs.get('session')

    def get_by_id(self, id: int) -> Project:
        return self.session.query(Project).get(id)

    def add_contract(self, contract: Contract, project: Project):
        project.contracts.append(contract)

    def active_contracts_count(self, project):
        count = self.session.query(Contract).filter(
            Contract.status == 'ACTIVE', Contract.project == project
        ).count()
        return count

    def create(self, name: str) -> Project:
        project = Project(name=name)
        self.session.add(project)
        self.session.commit()
        return project

    def list(self) -> list:
        projects = self.session.query(Project).all()
        return projects


