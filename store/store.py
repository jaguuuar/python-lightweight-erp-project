# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

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

        inputs = ui.get_inputs(['Choose option from menu ', 9], '')
        chose_menu_number = inputs[0]

        is_menu_stores = True
        while is_menu_stores:

            if chose_menu_number == "1":
                show_table(table)
                is_menu_stores = False
            elif chose_menu_number == "2":
                add(table)
                is_menu_stores = False
            elif chose_menu_number == "3":
                remove(table, ui.get_inputs(['Enter id: ', 6], 'Remove record'))
                is_menu_stores = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: ', 6], 'Update record'))
                is_menu_stores = False
            elif chose_menu_number == "5":
                result = get_counts_by_manufacturers(table)
                ui.print_result(result, "Number of games that are available of each manufacturer: ")
                is_menu_stores = False
            elif chose_menu_number == "6":
                list_labels = ['Which manufacturer you want to check? ', 1]
                manufacturer = ui.get_inputs(list_labels, 'One question for you! \n')
                result = get_average_by_manufacturer(table, manufacturer)
                ui.print_result(result, "Number of games that are available of each manufacturer: ")
                is_menu_stores = False
            elif chose_menu_number == "0":
                is_menu_stores = False
                is_not_main_menu = False


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['ID', 'TITLE', 'MANUFACTURER', 'PRICE', 'IN_STOCK']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    inputs = ['Enter title: ', 6, 'Enter manufacturer: ', 1,
    'Enter price: ', 2, 'Enter in stock: ', 2]

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
    inputs = ['Enter title: ', 6, 'Enter manufacturer: ', 1,
    'Enter price: ', 2, 'Enter in stock: ', 2]

    table = common.update_record(table, inputs, id_)

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturers = []
    for record in table:
        if record[2] not in manufacturers:
            manufacturers.append(record[2])

    games_counts = {}
    for manufacturer in manufacturers:
        counts_sum = 0
        for record in table:
            if manufacturer in record:
                counts_sum += 1
        games_counts[manufacturer] = counts_sum

    return games_counts


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    manufacturer = "".join(manufacturer).rstrip()
    stock_sum = 0
    game_count = 0
    for record in table:
        for element in record:
            if manufacturer in record:
                stock_sum += int(record[4])
                game_count += 1

    if game_count != 0 or stock_sum != 0:
        average_games_in_stock = round(stock_sum / game_count, 2)
    else:
        average_games_in_stock = 'No games for this manufacturer'

    return average_games_in_stock
