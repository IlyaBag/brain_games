from random import randrange


GAME_RULE = 'What is the result of the expression?'
RANGE_MIN = 1
RANGE_MAX = 100


def get_task():
    number1 = randrange(RANGE_MIN, RANGE_MAX)
    number2 = randrange(RANGE_MIN, RANGE_MAX)
    index = randrange(3)
    operators = ('+', '-', '*')

    task = f'{number1} {operators[index]} {number2}'

    if index == 0:
        result = number1 + number2
    if index == 1:
        result = number1 - number2
    if index == 2:
        result = number1 * number2

    return task, str(result)
