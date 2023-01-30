from random import randrange
from math import sqrt


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_MIN = 2
RANGE_MAX = 110


def is_prime(num):
    if num == 2:
        return True

    number_check_range = int(sqrt(num)) + 1
    for divisor in range(2, number_check_range):
        if num % divisor == 0:
            return False
    else:
        return True


def get_task():
    number = randrange(RANGE_MIN, RANGE_MAX)

    task = f'{number}'

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return task, correct_answer
