from random import randrange


GAME_RULE = 'What number is missing in the progression?'


def get_task():
    start = randrange(1, 51)
    com_dif = randrange(1, 6)  # common difference
    seq_length = randrange(5, 15)
    hidden_index = randrange(1, seq_length - 1)
    sequence = [start]

    for i in range(1, seq_length):
        start += com_dif
        sequence.append(start)

    result = sequence[hidden_index]

    sequence[hidden_index] = '..'
    task = ''
    for elem in sequence:
        task = f'{task} {elem}'

    return task.lstrip(), str(result)
