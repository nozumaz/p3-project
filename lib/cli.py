#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
# from models import Tasks

# create menu
def main():
    print("test")
    
    options = ["View", "Add", "Edit", "Delete"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


# initialize CLI
if __name__ == '__main__':
    
    main()
    
    # task_list = input("task, deadline: ")

