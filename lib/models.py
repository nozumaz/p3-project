# https://docs.sqlalchemy.org/en/14/orm/quickstart.html

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

task_category = Table(
    "tasks_categories",
    Base.metadata,
    Column("task_id", ForeignKey("tasks.id")),
    Column("category_id", ForeignKey("categories.id"))
)


# model name singular, table name plural
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    
    name = Column(String)
    date = Column(Date)

    categories = relationship("Category", secondary=task_category)

    def __repr__(self):
        return f"Task(id={self.id!r}, name={self.name!r}, fullname={self.date!r})"

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    tasks = relationship("Task", secondary=task_category)

    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name!r})"


# list methods useds to add categories, etc
