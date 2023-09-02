from datetime import datetime

from src.settings import Base

from sqlalchemy import Column, String, Integer, DateTime, MetaData
from sqlalchemy.orm import relationship


class Project(Base):
    __tablename__ = 'projects'
    metadata = Base.metadata

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    contracts = relationship("Contract", back_populates="project")


