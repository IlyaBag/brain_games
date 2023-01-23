from random import randrange
from math import sqrt


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_MIN = 2
RANGE_MAX = 110


def get_task():
    number = randrange(RANGE_MIN, RANGE_MAX)

    task = f'{number}'

    result = 'yes'
    if number > 2:
        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                result = 'no'
                break

    return task, result
