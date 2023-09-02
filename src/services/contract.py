from src.repositories.contract import ContractRepository
from src.services.base import BaseService


class ContractService(BaseService):
    repo = ContractRepository

    def submit(self, pk: int):
        self.repository.get_by_id(pk=pk)

    def print_contracts(self):
        contracts = self.list()
        print(f'Contract list: id -- name -- created at -- finished at -- project id')
        for contract in contracts:
            print(f'{contract.id}\t {contract.name}\t\t {contract.created_at}\t\t {contract.finished_at}\t\t {contract.project_id}')
