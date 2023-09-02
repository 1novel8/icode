from src.models.contract import Contract
from src.repositories.base import BaseRepository


class ContractRepository(BaseRepository):
    model = Contract
