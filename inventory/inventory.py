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
    table = data_manager.get_table_from_file('inventory/inventory.csv')

    is_not_main_menu = True
    while is_not_main_menu:

        inventory_manager_menu= [
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Get available items",
            "(6) Get average durability by manufacturers"]

        ui.print_menu("Inventory manager menu: ", inventory_manager_menu, "(0) Back to main menu")

        chose_menu_number = input()

        is_menu_inventory = True
        while is_menu_inventory:
            if chose_menu_number == "1":
                show_table(table)
                is_menu_inventory = False
            elif chose_menu_number == "2":
                table = add(table)
                is_menu_inventory = False
            elif chose_menu_number == "3":
                table = remove(table, ui.get_inputs(['Enter id: '], 'Remove record'))
                is_menu_inventory = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: '], 'Update record'))
                is_menu_inventory = False
            elif chose_menu_number == "5":
                result = get_available_items(table)
                ui.print_result(result, 'exceeded their durability')
                is_menu_inventory = False
            elif chose_menu_number == "6":
                get_average_durability_by_manufacturers(table)
                is_menu_inventory = False
            elif chose_menu_number == "0":
                is_menu_inventory = False
                is_not_main_menu = False


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['ID', 'NAME', 'MANUFACTURER', 'PURCHASE_DATE', 'DURABILITY']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    inputs = ['Enter name: ', 'Enter manufacturer: ',
    'Enter purchase date: ', 'Enter durability: ']

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
    inputs = ['Enter name: ', 'Enter manufacturer: ',
    'Enter purhase date: ','Enter durability: ']

    table = common.update_record(table, inputs, id_)

    return table


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):
    available_items = []
    for record in table:
        exceed_year = int(record[3]) + int(record[4])
        if exceed_year >= 2017:
            available_items.append(record)

    return available_items



# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    manufacturers = []
    for record in table:
        if record[2] not in manufacturers:
            manufacturers.append(record[2])

    average_durability = {}
    for manufacturer in manufacturers:
        durability_sum = 0
        manu_count = 0
        for record in table:
            if manufacturer in record:
                durability_sum += int(record[4])
                manu_count += 1
        average_durability[manufacturer] = round(durability_sum / manu_count, 2)

    return average_durability
