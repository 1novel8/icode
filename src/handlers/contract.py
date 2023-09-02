from src.services.contract import ContractService
from src.services.project import ProjectService

from src.settings import get_session


class ContractHandlersMixin:
    @get_session
    def contract_create(self, session):
        name = input('Input project name:')
        service = ContractService(session=session)
        contract = service.create(name=name)
        return contract

    @get_session
    def contract_list(self, session):
        service = ContractService(session=session)
        service.print_contracts()

    @get_session
    def contract_submit(self, session):
        service = ContractService(session=session)
        service.submit()
