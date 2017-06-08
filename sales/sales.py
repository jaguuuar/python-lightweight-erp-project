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
import sys
sys.path.append('/home/sylwia/Codecool/TW_after_checkpoint1/TW6/python-lightweight-erp-project-do_you_even_code_bro')
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
    table = data_manager.get_table_from_file('sales/sales.csv')


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
        

        is_menu_sales = True
        while is_menu_sales:
        
            if chose_menu_number == "1":
                show_table(table)
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

    inputs = ['Enter title: ', 'Enter price: ','Enter month: ','Enter day: ','Enter year: ']
    inputs_entered = ui.get_inputs(inputs,'Update your record')


    for element in table:
        if element[0] == id_:
            for j in range(0,5):
                element[j+1] = inputs_entered[j]

    data_manager.write_table_to_file("sales.csv", table)

    return table

pass

''' Above three lines should be deleted at the end of our coding!'''




# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):

    lowest = int(table[0][2])
    lowest_price = []

    for j in range(len(table)):
        element = table[j][2]
        if int(element) < int(lowest):
            lowest = element

    for i in range(len(table)):
        element = table[i][2]
        if element == lowest:
            lowest_price.append(table[i][1].upper())



    # insertion sort to find descending alphabetical order longest name
    for number in range (1, len(lowest_price)):
        current_number = lowest_price[number]
        element = number - 1

        while element >= 0 and lowest_price[element] > current_number:
            lowest_price[element+1] = lowest_price[element]
            element -=1

        lowest_price[element+1] = current_number


    for row in table:
        if lowest_price[0] == row[1].upper():
            id_ = row[0]

    return id_
'''table = data_manager.get_table_from_file('sales.csv')
get_lowest_price_item_id(table)'''


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
