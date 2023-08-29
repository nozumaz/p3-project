from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base=declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column("user_id", Integer, primary_key=True)
    name = Column("user_name", String)