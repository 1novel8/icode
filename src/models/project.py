from datetime import datetime

from src.settings import Base, engine
from src.models.contract import Contract

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    contracts = relationship("Contract", back_populates="project")


Base.metadata.create_all(engine)
