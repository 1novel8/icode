from datetime import datetime

from sqlalchemy.orm import relationship

from src.session import Base
from src.enums import Status

from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey


class Contract(Base):
    __tablename__ = 'contracts'
    metadata = Base.metadata

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    finished_at = Column(DateTime, nullable=True, default=None)
    status = Column(Enum(Status), default=Status.ROW, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship("Project", back_populates="contracts")

