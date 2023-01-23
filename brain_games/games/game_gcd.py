from random import randrange


GAME_RULE = 'Find the greatest common divisor of given numbers.'
RANGE_MIN = 1
RANGE_MAX = 100


def get_task():
    number1 = randrange(RANGE_MIN, RANGE_MAX)
    number2 = randrange(RANGE_MIN, RANGE_MAX)

    task = f'{number1} {number2}'

    if number1 == number2:
        return task, str(number1)

    check_range = max(number1, number2) // 2
    result = 1
    for i in range(2, check_range + 1):
        if number1 % i == 0 and number2 % i == 0:
            result = i

    return task, str(result)
