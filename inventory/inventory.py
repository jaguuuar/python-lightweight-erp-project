# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

    # you code

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
    # inputs = ['Enter id: ', 'Enter name: ', 'Enter manufacturer: ',
    # 'Enter purchase date: ', 'Enter durability: ']
    #
    # new_record = ui.get_inputs(inputs, 'Add new record')
    # table.append(new_record)
    #
    # return table

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

    #inputs = ['Enter id: ']
    #del_record = ui.get_inputs(inputs, 'Remove record')

    # for record in table:
    #     if record[0] == id_:
    #     table.remove(record)
    #
    # return table
    #
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

    inputs = ['Enter name of object: ', 'Enter name of manufacturer: ','Enter purhase date: ','Enter durability: ']
    inputs_entered = ui.get_inputs(inputs,'Update your record')


    for element in table:
        if element[0] == id_:
            for j in range(0,4):
                element[j+1] = inputs_entered[j]

    data_manager.write_table_to_file("inventory.csv", table)

    return table

''' Above three lines should be deleted at the end of our coding!'''

table = data_manager.get_table_from_file("inventory.csv")
us_input = ui.get_inputs(['Enter ID: '],"Hello there !!!")
print(update(table, us_input[0]))


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

table = data_manager.get_table_from_file('inventory.csv')
#ui.get_inputs(list_labels, title)
print(add(table))

#def string_test()
