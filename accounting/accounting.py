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

    is_not_main_menu = True
    while is_not_main_menu:

        accounting_manager_menu = [
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Which year max",
            "(6) Average amount"]

        ui.print_menu("Accounting manager menu: ", accounting_manager_menu, "(0) Back to main menu")
        
        chose_menu_number = input()
        table = data_manager.get_table_from_file('accounting/items.csv')

        is_menu_accounting = True
        while is_menu_accounting:
        

            if chose_menu_number == "1":
                show_table(table)
            elif chose_menu_number == "2":
                add(table)
                is_menu_accounting = False
            elif chose_menu_number == "3":
                remove(table, ui.get_inputs(['Enter id: '], 'Remove record'))
                is_menu_accounting = False
            elif chose_menu_number == "4":
                update(table, ui.get_inputs(['Enter id: '], 'Update record'))
            elif chose_menu_number == "5":
                which_year_max(table)
            elif chose_menu_number == "6":
                avg_amount(table, year)
            elif chose_menu_number == "0":
                is_menu_accounting = False 
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

#     inputs = ['Enter month: ', 'Enter day: ', 'Enter year:', 'Enter type: ', 'Enter amount: ']
#     inputs_entered = ui.get_inputs(inputs,'Update your record')
#
#
#     for element in table:
#         if element[0] == id_:
#             for j in range(0,5):
#                 element[j+1] = inputs_entered[j]
#
#     data_manager.write_table_to_file("customers.csv", table)
#
#     return table
#
#
# table = data_manager.get_table_from_file("items.csv")
# us_input = ui.get_inputs(['Enter ID: '],"hello")
#print(update(table, us_input[0]))

    pass



# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # in_list_2016 = []
    # out_list_2016 = []
    # in_list_2015 = []
    # out_list_2015 = []

    profit = {}


    for elements in table:
#        for year in range(1990,2018):
            #print(year)
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
    #
    #     elif elements[3] == "2015":
    #         if elements [4] == "in":
    #             in_list_2015.append(int(elements[5]))
    #         elif elements[4] == "out":
    #             out_list_2015.append(int(elements[5]))
    #
    # profit_2016 = sum(in_list_2016) - sum(out_list_2016)
    # profit_2015 = sum(in_list_2015) - sum(out_list_2015)
    #
    # if profit_2015 > profit_2016:
    #     answer = "2015"
    # elif profit_2016 > profit_2015:
    #     answer = "2016"

    print(profit)

table = data_manager.get_table_from_file("items.csv")
print(which_year_max(table))


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
