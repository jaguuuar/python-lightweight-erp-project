# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

    accounting_manager_menu = [
        "(1) Show table",
        "(2) Add",
        "(3) Remove",
        "(4) Update",
        "(5) Which year max",
        "(6) Average amount"]

    ui.print_menu("Accounting manager menu: ", accounting_manager_menu, "(0) Back to main menu")
    
    chose_menu_number = input()
    table = data_manager.get_table_from_file('accounting/items.csv')
    

    if chose_menu_number == "1":
        show_table(table)
    elif chose_menu_number == "2":
        add(table)
    elif chose_menu_number == "3":
        remove(table, ui.get_input(['Enter id: '], 'Remove record'))
    elif chose_menu_number == "4":
        update(table, ui.get_input(['Enter id: '], 'Update record'))
    elif chose_menu_number == "5":
        which_year_max(table)
    elif chose_menu_number == "6":
        avg_amount(table, year)
    elif chose_menu_number == "0":
        main.main()
    else:
        print("there is no number like that")
    
    pass



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

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
