def make_and_print_board(table, title_list):
    """
    This function find the longest word/ number lenght in every list of lists, than change all shorters

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints the board.
    """

    table.insert(0, title_list)
    columns = len(table[0])
    rows = len(table)
    columns_rows = []
    longests = []
    columns_rows_with_whitespace = []

    # make list with empty lists (it's depend on columns lenght)
    for i in range(0, columns):
        columns_rows.append([])
        columns_rows_with_whitespace.append([])
        for j in range(rows):
            columns_rows[i].append(table[j][i])     # add cells from columns to one list

    # found longest string or number in column and add them to list longests
    for i in range(len(columns_rows)):

        highest = len(str(columns_rows[i][0]))

        for element in columns_rows[i]:
            if highest < len(str(element)):
                highest = len(str(element))
        longests.append(highest)

    # add whitespaces and '|' to strings/numbers
    for i in range(len(columns_rows)):
        for element in columns_rows[i]:
            len_difference = longests[i] - len(str(element))
            rounded_up = ' '*int(len_difference/2)

            if len(str(element)) == longests[i]:
                element = '|  ' + str(element) + '  |'
            else:
                if (longests[i] - len(str(element))) % 2 == 0:
                    element = '|  ' + rounded_up + str(element) + rounded_up + '  |'
                else:
                    element = '|  ' + rounded_up + str(element) + rounded_up + ' ' + '  |'
            columns_rows_with_whitespace[i].append(element)

    back_to_rows = []

    for i in range(0, rows):
        back_to_rows.append([])

    # back to list of lists where sublist is row
    for i in range(len(back_to_rows)):
        for j in range(len(columns_rows_with_whitespace)):
            back_to_rows[i].append(columns_rows_with_whitespace[j][i])

    board_lines = []

    # make elements (lines with '-') beetween rows
    for element in longests:
        line = '-' + ((4+element) * '-') + '-'
        board_lines.append(line)

    temp = []

    for i in range(len(back_to_rows)):
        temp.append(back_to_rows[i])
        temp.append(board_lines)

    temp.insert(0, board_lines)
    table = temp

    for row in table:
        for element in row:
            print(element, end=' ')
        print(' ')


def print_table(table, title_list):

    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    make_and_print_board(table, title_list)
    table.remove(table[0])


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    if type(result) is dict:
        print (label)
        for keys, values in result.items():
            print(keys, values, end='\n\n')
        print('\n')

    elif type(result) is list:
        print(label)
        for lists in result:
            print(lists)
        print('\n')

    else:
        print('{}{}'.format(label, result))
        print('\n')


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """

    # list options from menu without brackets
    option_from_menu = ("\n ").join(list_options)

    print(title, "\n", option_from_menu, "\n", exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(title)
    for enter_input in list_labels:
        inputs.append(input(enter_input))

    return inputs

# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message


def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    message_error = "Error: @"
    print('{}{}'.format(message_error, message))
