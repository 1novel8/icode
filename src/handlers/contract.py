from src.services.contract import ContractService

from src.session import get_session


class ContractHandlersMixin:
    @get_session
    def contract_create(self, session):
        print('Создание контракта')
        name = input('Введите название контракта:')
        service = ContractService(session=session)
        contract = service.create(name=name)
        return contract

    @get_session
    def contract_list(self, session):
        service = ContractService(session=session)
        service.print_contracts()

    @get_session
    def contract_submit(self, session):
        print('Подтверждение контракта')
        service = ContractService(session=session)
        service.print_contracts()

        contract_id = int(input('Введите id контракта:'))
        service.submit(pk=contract_id)

    @get_session
    def contract_close(self, session):
            print('Закрытие контракта')
            service = ContractService(session=session)
            service.print_contracts()

            contract_id = int(input('Введите id контракта:'))
            service.close(pk=contract_id)

