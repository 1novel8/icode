from datetime import datetime

from src.enums import Status
from src.repositories.contract import ContractRepository
from src.services.base import BaseService


class ContractService(BaseService):
    repo = ContractRepository

    def submit(self, pk: int, **kwargs):
        contract = self.repository.get_by_id(pk=pk, **kwargs)
        self.repository.set_status(contract, status=Status.ACTIVE)

    def finish(self, pk: int):
        contract = self.repository.get_by_id(pk=pk)
        contract.finished_at(datetime.now())
        self.repository.set_status(contract, status=Status.FINISHED)

    def active_count(self, **kwargs):
        self.repository.active_count(**kwargs)

    def print_contracts(self):
        contracts = self.list()
        print(f'Contract list: id -- name  -- status -- created at -- finished at -- project id')
        for contract in contracts:
            print(f'{contract.id}\t {contract.name}\t\t {contract.status.value}\t\t {contract.created_at}\t\t {contract.finished_at}\t\t {contract.project_id}')
