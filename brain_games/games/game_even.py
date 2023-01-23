from random import randrange


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_MIN = 1
RANGE_MAX = 100


def get_task():
    number = randrange(RANGE_MIN, RANGE_MAX)

    result = 'no'
    if number % 2 == 0:
        result = 'yes'

    return number, result
