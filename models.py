from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base=declarative_base()

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column("task_id", Integer, primary_key=True)
    name = Column("task_name", String)