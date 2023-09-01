#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_term_menu import TerminalMenu
# from models import Tasks

# create menu
def main():
    print("test")
    
    options = ["View", "Add", "Edit", "Delete"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


    if terminal_menu[menu_entry_index] == "View":
        view(session, Task)


# initialize CLI
if __name__ == '__main__':


    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    main()
    session.close()
    
    # task_list = input("task, deadline: ")



def view(session, task):
    return session.query(task).order_by(task.date).all()
