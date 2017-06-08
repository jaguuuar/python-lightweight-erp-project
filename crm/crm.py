# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    table = data_manager.get_table_from_file('crm/customers.csv')

    is_not_main_menu = True
    while is_not_main_menu:

        customer_relationship_managment_menu =[
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Get longest name id",
            "(6) Get subscribed emails"]

        ui.print_menu("Customer relationship managment menu: ", customer_relationship_managment_menu, "(0) Back to main menu")

        inputs = ui.get_inputs(['Choose option from menu '], '')
        chose_menu_number = inputs[0]

        is_menu_crm = True
        while is_menu_crm:

            if chose_menu_number == "1":
                show_table(table)
                is_menu_crm = False
            elif chose_menu_number == "2":
                add(table)
                is_menu_crm = False
            elif chose_menu_number == "3":
                remove(table, ui.get_inputs(['Enter id: ', 6], 'Remove record'))
                is_menu_crm = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: ', 6], 'Update record'))
                is_menu_crm = False
            elif chose_menu_number == "5":
                result = get_longest_name_id(table)
                ui.print_result(result, 'The ID of the customer with the longest name: ')
                is_menu_crm = False
            elif chose_menu_number == "6":
                result = get_subscribed_emails(table)
                ui.print_result(result, 'Customers that subscribed to the newsletter: ')
                is_menu_crm = False
            elif chose_menu_number == "0":
                is_menu_crm = False
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

    title_list = ['ID', 'NAME', 'EMAIL', 'SUBSCRIBED']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    inputs = ['Enter name: ',1 , 'Enter email: ', 6,
    'Enter subscribed: ', 8]
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
    inputs = ['Enter name: ',1 , 'Enter email: ', 6,
    'Enter subscribed: ', 8]

    table = common.update_record(table, inputs, id_)

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # take from table column with names and add to customer_names list

    customer_names = [table[i][1] for i in range(len(table))]  # list with all names

    name = ""
    for row in table:
        if len(row[1]) > len(name):
            len_list = [table[i][1] for i in range(len(table)) if len(row[1]) == len(table[i][1])]  # list with the longest names
            name = row[1]
            # list with the longest names in big letters
            upper_list = [table[i][1].upper() for i in range(len(table)) if len(row[1]) == len(table[i][1])]



    # insertion sort to find descending alphabetical order longest name

    for number in range(1, len(upper_list)):
        current_number = upper_list[number]
        element = number - 1

        while element >= 0 and upper_list[element] > current_number:
            upper_list[element+1] = upper_list[element]
            element -= 1

        upper_list[element+1] = current_number

    # take id the longest name by descending alphabetical order
    for row in table:
        if upper_list[0] == row[1].upper():
            id_ = row[0]

    return id_

    # the question: Which customers has subscribed to the newsletter?
    # return type: list of strings (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):

    subscribed_to_newsletter_list = [table[i][2] + ";" + table[i][1] for i in range(len(table)) if table[i][3] == '1']  # list with all id 1, 0

    return(subscribed_to_newsletter_list)
