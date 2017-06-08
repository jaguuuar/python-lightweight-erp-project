# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

# importing everything you need
import os
import sys
sys.path.append('/home/grzegorz/Pulpit/code/python-lightweight-erp-project-do_you_even_code_bro')
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
    table = data_manager.get_table_from_file('store/games.csv')

    is_not_main_menu = True
    while is_not_main_menu:

        store_manager_menu = [
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Get counts by manufacturers",
            "(6) Get average by manufacturer"]

        ui.print_menu("Store manager menu: ", store_manager_menu, "(0) Back to main menu")

        chose_menu_number = input()
        
        
        is_menu_stores = True
        while is_menu_store:

            if chose_menu_number == "1":
                show_table(table)
            elif chose_menu_number == "2":
                add(table)
                is_menu_store = False
            elif chose_menu_number == "3":
                remove(table, ui.get_inputs(['Enter id: '], 'Remove record'))
                is_menu_store = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: '], 'Update record'))
            elif chose_menu_number == "5":
                get_counts_by_manufacturers(table)
            elif chose_menu_number == "6":
                get_average_by_manufacturer(table, manufacturer)
            elif chose_menu_number == "0":
                is_menu_store = False 
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

    # your code

    return table

    pass


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code

    return table

    pass


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    inputs = ['Enter title: ', 'Enter manufacturer: ','Enter price: ','Enter how many are in stock: ']
    inputs_entered = ui.get_inputs(inputs,'Update your record')


    for element in table:
        if element[0] == id_:
            for j in range(0,4):
                element[j+1] = inputs_entered[j]

    data_manager.write_table_to_file("store/games.csv", table)

    return table

''' Above three lines should be deleted at the end of our coding!'''

table = data_manager.get_table_from_file('store/games.csv')
us_input = ui.get_inputs(['Enter ID: '],"Hello there !!!")
print(update(table, us_input[0]))


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
