from datetime import datetime

from src.enums import Status
from src.models.contract import Contract
from src.repositories.contract import ContractRepository
from src.services.base import BaseService
from src.exceptions import (StatusException,
                            ContractNotAvailableException,
                            NoProjectRelatedException,
                            WrongProjectRelatedException)


class ContractService(BaseService):
    repo = ContractRepository

    def close(self, pk: int, **kwargs):
        contract = self.repository.get_by_id(pk=pk)
        if contract.status != Status.ACTIVE:
            raise StatusException

        project_id = kwargs.get('project_id', None)
        if contract.project_id is None:
            raise NoProjectRelatedException
        if contract.project_id != project_id:
            raise WrongProjectRelatedException

        self.repository.set_status(contract, status=Status.CLOSED)
        contract.finished_at = datetime.now()

    def submit(self, pk: int, **kwargs):
        contract = self.repository.get_by_id(pk=pk)
        if contract.status != Status.ROW:
            raise StatusException
        self.repository.set_status(contract, status=Status.ACTIVE)

    def active_count(self, **kwargs):
        return self.repository.active_count(**kwargs)

    def is_available(self, contract: Contract):
        if contract.status != Status.ACTIVE:
            raise StatusException
        if contract.finished_at is not None or contract.project_id is not None:
            raise ContractNotAvailableException

    def print_contracts(self):
        contracts = self.list()
        print(f'Список контрактов:\nid\t\t name\t\t status\t\t created at\t\t finished at\t\t project id')
        for contract in contracts:
            print(f'{contract.id}\t\t {contract.name}\t\t {contract.status.value}\t\t {contract.created_at}\t\t {contract.finished_at}\t\t {contract.project_id}')

    def list(self, **kwargs):
        return self.repository.list(**kwargs)

    def print_project_contracts(self, party_id: int):
        contracts = self.list(party_id=party_id)
        print(f'Список контрактов:\nid\t\t name\t\t status\t\t created at\t\t finished at\t\t project id')
        for contract in contracts:
            print(f'{contract.id}\t\t {contract.name}\t\t {contract.status.value}\t\t {contract.created_at}\t\t {contract.finished_at}\t\t {contract.project_id}')
