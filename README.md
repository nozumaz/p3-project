# p3-project
Python Command Line Project - Flatiron Phase 3

pipenv shell

- [Notes](./notes/notes.md)

1. create virtual environment (`pipenv --python 3.8.13`)
2. install dependencies (`pipenv install sqlalchemy==1.4.41 alembic ipdb faker`)
    a. SQLALchemy 1.4.41
    b. Alembic (migration manager)
    c. ipdb
    d. faker (to generate fake data)
3. create migration environment (after `pipenv shell`, `alembic init migrations`)
4. configure migration environment (alembic.ini and env.py) (sqlalchemy.url = sqlite:///events_tracker.db)
5. create declarative_base
6. create schema (python classes or models)
7. populate database with seeds
8. test relationships (one to many)