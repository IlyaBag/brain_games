import prompt


def play_round(game_name):
    question, correct_answer = game_name.get_task()
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')

    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. ", end='')
        print(f"Correct answer was '{correct_answer}'.")
        return False


def play_game(game_name):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game_name.GAME_RULE)
    for i in range(3):
        if not play_round(game_name):
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
