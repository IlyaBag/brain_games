from random import randrange


GAME_RULE = 'What is the result of the expression?'
RANGE_MIN = 1
RANGE_MAX = 100


def calculate(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    return result


def get_task():
    number1 = randrange(RANGE_MIN, RANGE_MAX)
    number2 = randrange(RANGE_MIN, RANGE_MAX)
    operators = ('+', '-', '*')
    index = randrange(len(operators))

    task = f'{number1} {operators[index]} {number2}'

    correct_answer = str(calculate(number1, number2, operators[index]))

    return task, correct_answer
