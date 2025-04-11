from sqlalchemy import Column, Integer, String, Boolean
from models.base import Base

class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)