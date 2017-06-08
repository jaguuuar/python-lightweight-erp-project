# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


'''# importing everything you need      ODKOMENTOWAC TE DOCSTRinGI!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common'''


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

        human_resources_manager_menu = [
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Get oldest person",
            "(6) Get persons closest to average"]

        ui.print_menu("Human resources manager menu: ", human_resources_manager_menu, "(0) Back to main menu")

        chose_menu_number = input()
        table = data_manager.get_table_from_file('hr/persons.csv')

        is_menu_hr = True
        while is_menu_hr:

            if chose_menu_number == "1":
                show_table(table)
            elif chose_menu_number == "2":
                add(table)
                is_menu_hr = False
            elif chose_menu_number == "3":
                remove(table, ui.get_inputs(['Enter id: '], 'Remove record'))
                is_menu_hr = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: '], 'Update record'))
            elif chose_menu_number == "5":
                get_oldest_person(table)
            elif chose_menu_number == "6":
                get_persons_closest_to_average(table)
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

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

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

    summed_age = 0
    list_with_age = []
    closest_to_average_age = []

    for j in range(len(table)):
        element = 2017 - int(table[j][2])
        list_with_age.append(element)
        summed_age += element

    print(list_with_age)
    average_age = round(summed_age/len(table))
    print(average_age)

    for i in range(len(list_with_age)):
        element = 2017 - int(table[i][2])
        temp = abs(2017 - int(table[i][2]) - average_age)
        print(temp)
        if element == average_age:
            closest_to_average_age.append(table[i][1])

        elif element > temp:
            temp = element
            closest_to_average_age.append(table[i][1])

    print(closest_to_average_age)


def main():

    with open('persons.csv', "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]

    print(get_oldest_person(table))
    get_persons_closest_to_average(table)

main()
