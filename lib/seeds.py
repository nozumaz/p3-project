from models import Task,Category,task_category    # You will need to import your own models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from datetime import datetime,time

engine = create_engine("sqlite:///events_tracker.db")
Session = sessionmaker(bind=engine)
session = Session() # Query the DB with session example: session.query(ModelOne).all()

# Use ipdb to interact with DB using session
import ipdb #; ipdb.set_trace() # # Dont forget to add ipdb as a dependency - pipenv install ipdb

# For generating Fake data: https://faker.readthedocs.io/en/master/providers.html
from faker import Faker 
import random

# For working with an API and retrieving json data
# import requests
# import json

# Example request
# response = requests.get(API_URL)
# json_data = json.loads(response.text)

session.query(Task).delete()
session.query(Category).delete()
session.query(task_category).delete()

# fake = Faker()

print("populate tasks tables")
tasks = [
    Task(
        name="test1",
        date=datetime.now()
    ),
    Task(
        name="test2",
        date=datetime.now()
    ),
    Task(
        name="test3",
        date=datetime.now()
    ),
    Task(
        name="test4",
        date=datetime.now()
    ),
    Task(
        name="test5",
        date=datetime.now()
    )
]

print("populate categories table")
categories = [
    Category(
        name="personal",
    ),
    Category(
        name="work",
    ),
    Category(
        name="shopping",
    )
]

session.add_all(tasks)
session.add_all(categories)
session.commit()




for task in tasks:
    #for i in range(len(tasks)):
    task.categories.append(random.choice(categories))
        #categories = Categories(
        #   name="category1"
        #)

session.commit()

# .



# tasks.categories.append(categories)

ipdb.set_trace()

print("finished seeding")
