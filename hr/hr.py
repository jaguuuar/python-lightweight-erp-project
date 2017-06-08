# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    is_not_main_menu = True
    while is_not_main_menu:

        human_resources_manager_menu = [
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Get oldest person",
            "(6) Get persons closest to average"]

        ui.print_menu("Human resources manager menu: ", human_resources_manager_menu, "(0) Back to main menu")

        chose_menu_number = input()
        table = data_manager.get_table_from_file('hr/persons.csv')

        is_menu_hr = True
        while is_menu_hr:

            if chose_menu_number == "1":
                show_table(table)
            elif chose_menu_number == "2":
                add(table)
                is_menu_hr = False
            elif chose_menu_number == "3":
                remove(table, ui.get_inputs(['Enter id: '], 'Remove record'))
                is_menu_hr = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: '], 'Update record'))
                is_menu_hr = False
            elif chose_menu_number == "5":
                get_oldest_person(table)
                is_menu_hr = False
            elif chose_menu_number == "6":
                get_persons_closest_to_average(table)
                is_menu_hr = False
            elif chose_menu_number == "0":
                is_menu_hr = False
                is_not_main_menu = False



def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    inputs = ['Enter name: ', 'Enter birth date: ']
    table = common.add_record(table, inputs)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """
    table = common.remove_record(table, id_)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
