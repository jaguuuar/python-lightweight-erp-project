# implement commonly used functions here

import random
import string
import ui


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    id_list=[]
    for record in table:
        id_list.append(record[0])

    while True:
        generated = []
        for i in range(2):
            number = random.randint(0,9)
            generated.append(str(number))
            upper = random.choice(string.ascii_uppercase)
            generated.append(upper)
            lower = random.choice(string.ascii_lowercase)
            generated.append(lower)
            char = random.choice(string.punctuation)
            while char == ';':
                char = random.choice(string.punctuation)
            generated.append(char)

        random.shuffle(generated)
        generated = ''.join(generated)
        if generated not in id_list:
            break

    return generated

def add_record(table, inputs_list):
    new_id = generate_random(table)
    new_record = ui.get_inputs(inputs_list, 'Add new record')
    new_record.insert(0,new_id)
    table.append(new_record)

    return table


def remove_record(table, id_):
    id_ = ''.join(id_)
    for record in table:
        if record[0] == id_:
            table.remove(record)

    return table


def update_record(table, inputs, id_):
    for record in table:
        if record[0] == ''.join(id_):
            inputs_entered = ui.get_inputs(inputs,'Update your record')
            for element in range(len(inputs)):
                record[element+1] = inputs_entered[element]

    return table
