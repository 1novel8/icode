from src.models.contract import Contract
from src.repositories.contract import ContractRepository


class ContractService:
    def __init__(self, **kwargs):
        self.repository = ContractRepository(session=kwargs.get('session'))

    def create(self, name: str) -> Contract:
        return self.repository.create(name=name)

    def get_by_id(self, id: int) -> Contract:
        return self.repository.get_by_id(id=id)

    def list(self) -> list:
        return self.repository.list()

    def print_contracts(self):
        contracts = self.list()
        print(f'Contract list: id -- name -- created at -- finished at -- project id')
        for contract in contracts:
            print(f'{contract.id}\t {contract.name}\t\t {contract.created_at}\t\t {contract.finished_at}\t\t {contract.project_id}')
