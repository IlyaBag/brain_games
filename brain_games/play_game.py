import prompt
import importlib


def play_round(game_name):
    module = importlib.import_module(game_name)

    question, correct_answer = module.get_task()
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
    module = importlib.import_module(game_name)

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(module.game_rule)
    for i in range(3):
        if not play_round(game_name):
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
