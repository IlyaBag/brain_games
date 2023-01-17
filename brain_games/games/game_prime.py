from random import randrange
from math import sqrt


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task():
    number = randrange(2, 110)

    task = f'{number}'

    result = 'yes'
    if number > 2:
        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                result = 'no'
                break

    return task, result
