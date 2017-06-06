# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

    # you code
    inventory_manager_menu= [
        "(1) Show table",
        "(2) Add",
        "(3) Remove",
        "(4) Update",
        "(5) Get available items",
        "(6) Get average durability by manufacturers"]

    ui.print_menu("Inventory manager menu: ", inventory_manager_menu, "(0) Back to main menu")


    chose_menu_number = input()
    table = data_manager.get_table_from_file('inventory/inventory.csv')


    if chose_menu_number == "1":
        show_table(table)
    elif chose_menu_number == "2":
        add(table)
    elif chose_menu_number == "3":
        remove(table, ui.get_input(['Enter id: '], 'Remove record'))
    elif chose_menu_number == "4":
        update(table, ui.get_input(['Enter id: '], 'Update record'))
    elif chose_menu_number == "5":
        get_available_items(table)
    elif chose_menu_number == "6":
        get_average_durability_by_manufacturers(table)
    elif chose_menu_number == "0":
        main.main()
    else:
        print("there is no number like that")


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

    inputs = ['Enter id: ', 'Enter name: ', 'Enter manufacturer: ',
    'Enter purchase date: ', 'Enter durability: ']

    new_record = ui.get_inputs(inputs, 'Add new record')
    table.append(new_record)


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

    id_ = ''.join(id_)

    for record in table:
        if record[0] == id_:
            table.remove(record)

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

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):

    # your code

    pass


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
