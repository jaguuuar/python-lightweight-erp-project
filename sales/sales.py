# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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

        sales_manager_menu =[
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Get lowest price item id",
            "(6) Get items sold between"]

        ui.print_menu("Sales manager menu: ", sales_manager_menu , "(0) Back to main menu")


        chose_menu_number = input()
        table = data_manager.get_table_from_file('sales/sales.csv')

        is_menu_sales = True
        while is_menu_sales:

            if chose_menu_number == "1":
                show_table(table)
                is_menu_sales = False
            elif chose_menu_number == "2":
                add(table)
                is_menu_sales = False
            elif chose_menu_number == "3":
                remove(table, ui.get_inputs(['Enter id: '], 'Remove record'))
                is_menu_sales = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: '], 'Update record'))
            elif chose_menu_number == "5":
                get_lowest_price_item_id(table)
            elif chose_menu_number == "6":
                get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
            elif chose_menu_number == "0":
                is_menu_sales = False
                is_not_main_menu = False


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['ID', 'TITLE', 'PRICE', 'MONTH', 'DAY', 'YEAR']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    inputs = ['Enter title: ', 'Enter price: ',
    'Enter month: ', 'Enter day: ', 'Enter year: ']
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

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):

    # your code

    pass


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
