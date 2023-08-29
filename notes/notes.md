# Phase 3 Python Command Line Project Notes

- [P3 Project Requirements](https://my.learn.co/courses/653/pages/phase-3-project-cli?module_item_id=95439)

### minimum requirements

- A CLI application
    - solves a real-world problem
    - adheres to best practices.
- A database created and modified with SQLAlchemy ORM with 2+ related tables.
- A well-maintained virtual environment using Pipenv.
- Proper package structure in your application.
- Use of lists and dicts.

### stretch goals

- A database created and modified with SQLAlchemy ORM with 3+ related tables.
- Use of many-to-many relationships with SQLAlchemy ORM.
- Use of additional data structures, such as ranges and tuples.



## steps
1. create virtual environment (`pipenv --python 3.8.13`)
2. install dependencies (`pipenv install sqlalchemy==1.4.41 alembic ipdb faker`)
    a. SQLALchemy 1.4.41
    b. Alembic (migration manager)
    c. ipdb
    d. faker (to generate fake data)
3. create migration environment (after `pipenv shell`, `alembic init migrations`)
4. configure migration environment (alembic.ini and env.py) (sqlalchemy.url = sqlite:///events_tracker.db) (made some updates to env.py)
5. create declarative_base
6. create schema (python classes or models)
7. populate database with seeds
8. test relationships (one to many)

tables
 - tasks


## Project Pitch

### Main idea
To Do List application that user can updated through Command Line Interface

### User story
- User is runs executable file which asks user for any `Task` they want to complete and `Deadline` to complete by
- `Category` classification in case the To Do list needs to be filtered out
- User can also delete or update tasks as necessary

### Use of Concepts
#### Object Oriented Python
> *Describe how you plan to use Python Classes and Objects to model your application*
- Classes will be used to create the tables for the tasks and categories

#### Database Tables
> *Describe how you will use SQLAlchemy to create and interact with 2 or more related database tables*
- `Task` table holds task id, task name, deadline, category

#### Object Relationships
> *Describe the types of relationships your different classes and tables will have with each other*
- Tables will be created from classes that can be used to quickly create new tables

#### Aggregate and Association Methods
> *Describe a few of the methods you plan on including in your application to query your database*
- User types command:
    - `view` to see the list of task items
    - `edit` to edit item
    - `delete` to delete item

#### Use of Data Structures
> *Describe how you plan on using data structures like lists and dictionaries in your project*
- A list can be used to collect the data that is stored into the database
- Dict can be used to collect data that would originate from a key



### Challenges
> *Describe which aspect of the project you think will present the greatest challenge, or the topic that you feel least familiar with at present.*
- Using Python and SQL

