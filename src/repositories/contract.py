from src.models.contract import Contract


class ContractRepository:
    def __init__(self, **kwargs):
        self.session = kwargs.get('session')

    def get_by_id(self, id: int) -> Contract:
        return self.session.query(Contract).get(id)

    def create(self, name: str) -> Contract:
        contract = Contract(name=name)
        self.session.add(contract)
        self.session.commit()
        return contract

    def list(self) -> list:
        contracts = self.session.query(Contract).all()
        return contracts