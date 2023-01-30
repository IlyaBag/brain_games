from random import randrange


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_MIN = 1
RANGE_MAX = 100


def is_even(num):
    return num % 2 == 0


def get_task():
    number = randrange(RANGE_MIN, RANGE_MAX)

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return number, correct_answer
