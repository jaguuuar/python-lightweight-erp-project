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

        inputs = ui.get_inputs(['Choose option from menu '], '')
        chose_menu_number = inputs[0]

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
                is_menu_sales = False

            elif chose_menu_number == "5":
                result = get_lowest_price_item_id(table)

                ui.print_result(result, 'The id of lowest price: \n')
                is_menu_sales = False

            elif chose_menu_number == "6":
                questions_list = ['Enter initial month ', 'Enter initial day ', 'Enter initial year ',
                                  'Enter final month ', 'Enter final day ', 'Enter final year ']

                inputs_list = ui.get_inputs(questions_list, 'Enter a time')
                result = get_items_sold_between(table, inputs_list[0], inputs_list[1], inputs_list[2], inputs_list[3],
                                                inputs_list[4], inputs_list[5])
                ui.print_result(result, 'Items in part of time: \n')
                is_menu_sales = False

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
    inputs = ['Enter title: ', 'Enter price: ',
    'Enter month: ', 'Enter day: ', 'Enter year: ']

    table = common.update_record(table, inputs, id_)

    return table


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
    for number in range(1, len(lowest_price)):
        current_number = lowest_price[number]
        element = number - 1

        while element >= 0 and lowest_price[element] > current_number:
            lowest_price[element+1] = lowest_price[element]
            element -= 1

        lowest_price[element+1] = current_number

    for row in table:
        if lowest_price[0] == row[1].upper():
            id_ = row[0]

    return id_


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    if len(str(day_from)) < 2:
        day_from = '0' + str(day_from)
    if len(str(day_to)) < 2:
        day_to = '0' + str(day_to)
    if len(str(month_from)) < 2:
        month_from = '0' + str(month_from)
    if len(str(month_to)) < 2:
        month_to = '0' + str(month_to)

    date_from = str(year_from) + str(month_from) + str(day_from)
    date_to = str(year_to) + str(month_to) + str(day_to)


    dict_with_all_rows = {}
    sorted_list = []
    for i in range(len(table)):
        if len(table[i][4]) < 2:
            table[i][4] = '0' + str(table[i][4])
        if len(table[i][3]) < 2:
            table[i][3] = '0' + str(table[i][3])

        dict_with_all_rows[(table[i][0], table[i][1], table[i][2])] = str(table[i][5]) + str(table[i][3]) + str(table[i][4])

    for key, value in dict_with_all_rows.items():
        if int(value) > int(date_from) and int(value) < int(date_to):
            sorted_list.append([key[0], key[1], int(key[2]), int(dict_with_all_rows[key][4:6]), int(dict_with_all_rows[key][6:]),
                                int(dict_with_all_rows[key][:4])])

    return(sorted_list)
