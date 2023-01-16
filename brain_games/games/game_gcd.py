from random import randrange


game_rule = 'Find the greatest common divisor of given numbers.'


def get_task():
    number1 = randrange(1, 100)
    number2 = randrange(1, 100)

    task = f'{number1} {number2}'

    if number1 == number2:
        return task, str(number1)

    check_range = max(number1, number2) // 2
    result = 1
    for i in range(2, check_range + 1):
        if number1 % i == 0 and number2 % i == 0:
            result = i

    return task, str(result)
