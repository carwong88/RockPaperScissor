# Player Class

import random
from rps_util import validate_secret_input


MOVES = ['rock', 'paper', 'scissors']


class Player:
    scores = 0

    def __init__(self, name=''):
        self.name = name
        self.prev_move = ''
        self.last_move = ''
        self.wins = False
        self.opp_last_move = ''

    def move(self):
        self.last_move = 'rock'

    def learn(self, opp_move):
        self.opp_last_move = opp_move


class RockPlayer(Player):
    def __init__(self, name='Computer'):
        super().__init__(name)

    def move(self):
        self.last_move = 'rock'


class RandomPlayer(Player):
    def __init__(self, name='Computer'):
        super().__init__(name)

    def move(self):
        self.last_move = random.choice(MOVES)


class ReflectPlayer(Player):
    def __init__(self, name='Computer'):
        super().__init__(name)

    def move(self):
        if not self.last_move:
            self.last_move = random.choice(MOVES)
        else:
            self.last_move = self.opp_last_move


class CyclePlayer(Player):
    def __init__(self, name='Computer'):
        super().__init__(name)

    def move(self):
        if not self.last_move:
            self.last_move = random.choice(MOVES)
        else:
            index = [i for i, val in enumerate(MOVES) if
                     val in self.last_move][0]
            if index >= len(MOVES)-1:
                self.last_move = MOVES[0]
            else:
                self.last_move = MOVES[index+1]


class HumanPlayer(Player):
    def __init__(self, name='You'):
        super().__init__(name)

    def move(self):
        self.last_move = validate_secret_input(
            f'{self.name}: Rock, paper, scissors? ', MOVES)
