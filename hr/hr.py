# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
    table = data_manager.get_table_from_file('hr/persons.csv')

    is_not_main_menu = True
    while is_not_main_menu:
        data_manager.write_table_to_file('hr/persons.csv', table)
        human_resources_manager_menu = [
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Get oldest person",
            "(6) Get persons closest to average"]

        ui.print_menu("Human resources manager menu: ", human_resources_manager_menu, "(0) Back to main menu")

        inputs = ui.get_inputs(['Choose option from menu ', 9], '')
        chose_menu_number = inputs[0]

        is_menu_hr = True
        while is_menu_hr:

            if chose_menu_number == "1":
                show_table(table)
                is_menu_hr = False
            elif chose_menu_number == "2":
                add(table)
                is_menu_hr = False
            elif chose_menu_number == "3":
                remove(table, ui.get_inputs(['Enter id: ', 6], 'Remove record'))
                is_menu_hr = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: ', 6], 'Update record'))
                is_menu_hr = False
            elif chose_menu_number == "5":
                result = get_oldest_person(table)
                ui.print_result(result, 'The oldest person is (or are): \n')
                is_menu_hr = False
            elif chose_menu_number == "6":
                result = get_persons_closest_to_average(table)
                ui.print_result(result, 'Person closest to the average age is (or are): \n')
                is_menu_hr = False
            elif chose_menu_number == "0":
                is_menu_hr = False
                is_not_main_menu = False


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['ID', 'NAME', 'BIRTH_DATE']
    ui.print_table(table, title_list)

    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    inputs = ['Enter name: ', 1, 'Enter birth date: ', 3]
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
    inputs = ['Enter name: ', 1, 'Enter birth date: ', 3]

    table = common.update_record(table, inputs, id_)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    """
    Find oldest person/people from table

    Args:
        table: list of lists which contains id, person name and birth year

    Returns:
        oldest_people: list of strings (oldest people)
    """

    oldest = int(table[0][2])
    oldest_people = []

    for j in range(len(table)):
        element = table[j][2]
        if int(element) < int(oldest):
            oldest = element
            name = table[j][1]

    for i in range(len(table)):
        element = table[i][2]
        if element == oldest:
            oldest_people.append(table[i][1])

    return oldest_people


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    """
    Find person closest to the average age

    Args:
        table: list of lists which contains id, person name and birth year

    Returns:
        closest_to_average_age: list of strings (names people closest to average)
    """

    summed_age = 0
    list_with_age = []
    closest_to_average_age = []

    for j in range(len(table)):
        element = 2017 - int(table[j][2])
        list_with_age.append(element)
        summed_age += element

    average_age = round(summed_age/len(table))

    closest_to_average = []
    to_compare = abs(2017 - int(table[0][2]) - average_age)

    for i in range(len(list_with_age)):
        element = 2017 - int(table[i][2])
        temp = abs(element - average_age)

        if temp < to_compare:
            to_compare = temp
            closest_to_average.append(table[i][1])

    return closest_to_average
