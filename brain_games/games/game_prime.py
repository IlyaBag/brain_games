from random import randrange
from math import sqrt


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_MIN = 2
RANGE_MAX = 110


def get_task():
    number = randrange(RANGE_MIN, RANGE_MAX)

    task = f'{number}'

    if number == 2:
        result = 'yes'
        return task, result

    number_check_range = int(sqrt(number)) + 1
    for divisor in range(2, number_check_range):
        if number % divisor == 0:
            result = 'no'
            break
    else:
       result = 'yes' 

    return task, result
