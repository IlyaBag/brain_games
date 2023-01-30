from random import randrange


GAME_RULE = 'What number is missing in the progression?'


def hide_sequence_element(items):
    hidden_index = randrange(1, len(items) - 2)
    hidden_elem = items[hidden_index]

    items[hidden_index] = '..'
    hid_elem_items = ''
    for elem in items:
        hid_elem_items = f'{hid_elem_items} {elem}'

    return hid_elem_items.lstrip(), hidden_elem


def get_task():
    start = randrange(1, 51)
    com_dif = randrange(1, 6)  # common difference of an arithmetic sequence
    seq_length = randrange(5, 15)

    sequence = [start]
    for _ in range(1, seq_length):
        start += com_dif
        sequence.append(start)

    task, result = hide_sequence_element(sequence)

    return task, str(result)
