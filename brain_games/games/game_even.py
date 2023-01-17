from random import randrange


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task():
    number = randrange(1, 100)

    result = 'no'
    if number % 2 == 0:
        result = 'yes'

    return number, result
