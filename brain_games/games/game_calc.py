from random import randrange


GAME_RULE = 'What is the result of the expression?'


def get_task():
    number1 = randrange(1, 100)
    number2 = randrange(1, 100)
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
