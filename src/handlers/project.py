from src.exceptions import ContractNotAvailableException, NoActiveContractsException, ActiveContractsLimitException
from src.services.contract import ContractService
from src.services.project import ProjectService
from src.settings import get_session


class ProjectHandlersMixin:
    @get_session
    def project_create(self, session):
        contract_service = ContractService(session=session)
        if contract_service.active_count() == 0:
            raise NoActiveContractsException

        name = input('Input project name:')
        project_service = ProjectService(session=session)
        project_service.create(name=name)

    @get_session
    def project_list(self, session):
        service = ProjectService(session=session)
        service.print_projects()

    @get_session
    def project_add_contract(self, session):
        contract_service = ContractService(session=session)
        project_service = ProjectService(session=session)

        print('Добавление договора к проекту')
        try:
            project_service.print_projects()
            project_id = int(input('Введите id проекта'))
            project = project_service.get_by_id(project_id)

            if contract_service.active_count(project_id=project_id) > 1:
                raise ActiveContractsLimitException

            contract_service.print_contracts()
            contract_id = int(input('Введите id договора'))
            contract = contract_service.get_by_id(contract_id)
            contract_service.is_available(contract)

            project_service.add_contract(contract=contract, project=project)

        except ActiveContractsLimitException:
            print('!!!У вас уже есть незавершенный договор!!!')
        except ContractNotAvailableException:
            print('!!!Контракт уже занят!!!')

    @get_session
    def project_close_contract(self, session):
        contract_service = ContractService(session=session)
        project_service = ProjectService(session=session)

        print('Закрытие договора')
        project_service.print_projects()
        project_id = int(input('Введите id проекта'))
        project = project_service.get_by_id(project_id)

        contract_service.print_project_contracts(project_id)
        contract_id = int(input('Введите id договора'))
        contract = contract_service.get_by_id(contract_id)

        contract_service.close(pk=contract_id)
