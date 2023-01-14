from random import randrange
import prompt
# from brain_games.cli import *


def play_round_even():
    number = randrange(1, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')

    correct_answer = 'no'
    if number % 2 == 0:
        correct_answer = 'yes'

    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. ", end='')
        print(f"Correct answer was '{correct_answer}'.")
        return False


def play_game_even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        if not play_round_even():
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
