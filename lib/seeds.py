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
# from faker import Faker 
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
        name="take dog on a walk",
        date=datetime.now()
    ),
    Task(
        name="buy groceries",
        date=datetime.now()
    ),
    Task(
        name="study",
        date=datetime.now()
    ),
    Task(
        name="clean",
        date=datetime.now()
    ),
    Task(
        name="read",
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
    ),
    Category(
        name="chores",
    ),
    Category(
        name="misc",
    )
]

session.add_all(tasks)
session.add_all(categories)
session.commit()




""" for task in tasks:
    #for i in range(len(tasks)):
    task.categories.append(random.choice(categories))
        #categories = Categories(
        #   name="category1"
        #) """

session.commit()

# .

ipdb.set_trace()

print("finished seeding")
