#!/usr/bin/env python3

from models import Task, Category, view

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_term_menu import TerminalMenu



# create menu
def main():
    print("test")
    
    options = ["View", "Add", "Edit", "Delete"]
    terminal_menu = TerminalMenu(options)

    while True:
        print()

        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")


        if options[menu_entry_index] == "View":
            print(f"viewing")
            view(session, Task)


# initialize CLI
if __name__ == '__main__':


    engine = create_engine('sqlite:///events_tracker.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    main()
    session.close()
    
    # task_list = input("task, deadline: ")



