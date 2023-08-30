import datetime

from pydantic import BaseModel

from src.enums import Status


class ContractSchema(BaseModel):
    name: str
    created_at: datetime.datetime
    finished_at: datetime.datetime
    status: Status
    project_id: int
