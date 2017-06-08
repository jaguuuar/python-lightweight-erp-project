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

    inputs = ['Enter month: ', 'Enter day: ', 'Enter year:', 'Enter type: ', 'Enter amount: ']
    inputs_entered = ui.get_inputs(inputs,'Update your record')


    for element in table:
        if element[0] == id_:
            for j in range(0,5):
                element[j+1] = inputs_entered[j]

    data_manager.write_table_to_file("customers.csv", table)

    return table
#
#
# table = data_manager.get_table_from_file("items.csv")
# us_input = ui.get_inputs(['Enter ID: '],"hello")
# print(update(table, us_input[0]))



# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    profit = {}
    profit_values = []
    year_max = []


    for elements in table:
            if elements[3] not in profit:
                profit.update({elements[3] : 0})
                if elements [4] == "in":
                    profit[elements[3]] += (int(elements[5]))
                elif elements[4] == "out":
                    profit[elements[3]] += (-1 * int(elements[5]))
            elif elements[3] in profit:
                if elements [4] == "in":
                    profit[elements[3]] += (int(elements[5]))
                elif elements[4] == "out":
                    profit[elements[3]] += (-1 * int(elements[5]))

    for value in profit.values():
        profit_values.append(value)

    for i in range(0,len(profit_values)-1):
        for j in range(0,len(profit_values)-1-i):
            if profit_values[j] > profit_values[j+1]:
                temp = profit_values[j]
                profit_values[j] = profit_values[j+1]
                profit_values[j+1] = temp
    max_value = profit_values[len(profit_values)-1]

    for key, value in profit.items():
        if value == max_value:
            year_max.append(key)

    year_max_number = int(year_max[0])

    return year_max_number


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    profit = {}
    items_count = 0

    for elements in table:
            if elements[3] not in profit:
                profit.update({elements[3] : 0})
                if elements [4] == "in":
                    profit[elements[3]] += (int(elements[5]))
                elif elements[4] == "out":
                    profit[elements[3]] += (-1 * int(elements[5]))
            elif elements[3] in profit:
                if elements [4] == "in":
                    profit[elements[3]] += (int(elements[5]))
                elif elements[4] == "out":
                    profit[elements[3]] += (-1 * int(elements[5]))
    for elements in table:
        if year in elements[3]:
            items_count += 1

    average_amount_per_item = int((profit[year]))/items_count

    return average_amount_per_item

#przy wywoływaniu funkcji trzeba dodać input do roku!
