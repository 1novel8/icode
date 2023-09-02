from src.services.contract import ContractService
from src.services.project import ProjectService
from src.settings import get_session


class ProjectHandlersMixin:
    @get_session
    def project_create(self, session):
        contract_service = ContractService(session=session)
        contract_service.active_count()
        name = input('Input project name:')
        project_service = ProjectService(session=session)
        project = project_service.create(name=name)

    @get_session
    def project_list(self, session):
        service = ProjectService(session=session)
        service.print_projects()

    @get_session
    def add_contract(self, session):
        contract_service = ContractService(session=session)
        project_service = ProjectService(session=session)
        contract_service.print_contracts()
        project_service.print_projects()

        print('Adding contract to project')
        try:
            contract_id = int(input('Enter contract id'))
            project_id = int(input('Enter project id'))

            contract = contract_service.get_by_id(contract_id)
            project = project_service.get_by_id(project_id)

            project_service.add_contract(contract, project)
        except ValueError:
            print('Данные введены некорректно')
