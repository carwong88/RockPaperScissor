"""
Udacity: Intro to Programming Nanodegree Program
Project: Rock Paper Scissors

This program plays the game of Rock, Paper, Scissors between two Players
(human or computer), and reports both Player's scores for each round and at
the end of the game.
"""

import random
from rps_players import (RockPlayer, RandomPlayer, ReflectPlayer,
                         CyclePlayer, HumanPlayer)
from game import PaperScissorsRock
from rps_util import validate_int_input


MAX_WIDTH = 65
MIN_WIDTH = 50
MOVES = ['rock', 'paper', 'scissors']
RANDOM_PLAYERS = [RandomPlayer, CyclePlayer, RockPlayer, ReflectPlayer]


def random_computer_player(players, name):
    idx = random.randint(0, len(players)-1)
    player = players.pop(idx)(name)
    return players, player


def random_computer_players():
    players, p1 = random_computer_player(RANDOM_PLAYERS, 'Computer 1')
    players, p2 = random_computer_player(players, 'Computer 2')
    return p1, p2


def play_by_computer(rounds):
    p1, p2 = random_computer_players()
    game = PaperScissorsRock(p1, p2, rounds)
    game.play_game()


def play_with_computer(rounds):
    p1 = HumanPlayer('You')
    _, p2 = random_computer_player(RANDOM_PLAYERS, 'Computer 1')
    game = PaperScissorsRock(p1, p2, rounds)
    game.play_game()


def play_with_friend(rounds):
    p1 = HumanPlayer('You')
    p2 = HumanPlayer('Friend')
    game = PaperScissorsRock(p1, p2, rounds)
    game.play_game()


def menu():
    print('')
    print('*'*MAX_WIDTH)
    print('Paper, Scissors, Rock'.upper().center(60))
    print('\n\tWhat do you want to do?\n'
          '\t1. Watch the computer play\n'
          '\t2. Play with the computer\n'
          '\t3. Play with a friend\n')


def start():
    menu()
    resp = validate_int_input('\tPlease enter 1, 2, or 3: ', [1, 2, 3])
    rounds = validate_int_input('\tHow many rounds do you want to play '
                                '(up to 10)? ', range(1, 11))

    if resp == 1:
        play_by_computer(rounds)
    elif resp == 2:
        play_with_computer(rounds)
    elif resp == 3:
        play_with_friend(rounds)


if __name__ == '__main__':
    start()
