# implement commonly used functions here

import random


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

    #generated = ''


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

    # your code

    return generated
