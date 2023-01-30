from random import randrange


GAME_RULE = 'Find the greatest common divisor of given numbers.'
RANGE_MIN = 1
RANGE_MAX = 100


def find_gcd(num1, num2):
    if num1 == num2:
        return num1

    check_range = max(num1, num2) // 2
    result = 1
    for i in range(2, check_range + 1):
        if num1 % i == 0 and num2 % i == 0:
            result = i
    return result


def get_task():
    number1 = randrange(RANGE_MIN, RANGE_MAX)
    number2 = randrange(RANGE_MIN, RANGE_MAX)

    task = f'{number1} {number2}'

    correct_answer = str(find_gcd(number1, number2))

    return task, correct_answer
