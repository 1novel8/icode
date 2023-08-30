import datetime

from pydantic import BaseModel

from src.models.project import Project


class ProjectSchema(BaseModel):
    name: str
    created_at: datetime.datetime

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.created_at = kwargs.get('created_at', None)

