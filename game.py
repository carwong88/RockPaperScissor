# Game Class

from rps_util import print_wait

MAX_WIDTH = 65
MIN_WIDTH = 50


class Game:
    rounds_count = 1
    total_rounds = 1

    def __init__(self, p1, p2, rounds=1):
        self.p1 = p1
        self.p2 = p2
        self.total_rounds = rounds

    def play_round(self):
        pass

    def play_game(self):
        pass

    def beats(self):
        pass


class PaperScissorsRock(Game):
    def print_round_wins(self):
        if self.p1.last_move == self.p2.last_move:
            print(f'This round is tie.'.upper().center(MIN_WIDTH))
        elif self.p1.wins:
            print(f'{self.p1.name} wins this '
                  f'round.'.upper().center(MIN_WIDTH))
        else:
            print(f'{self.p2.name} wins this '
                  f'round.'.upper().center(MIN_WIDTH))

        print_wait(f'{self.p1.name} Score: {self.p1.scores}, '
                   f'{self.p2.name} Score: {self.p2.scores}'.center(MIN_WIDTH))

    def print_game_over(self):
        spaces = (MAX_WIDTH - len(' game over '))//2
        ties = self.total_rounds - (self.p1.scores + self.p2.scores)
        print(f"\n{'*'*spaces} GAME OVER {'*'*spaces}")
        print(f'Total {self.total_rounds} round(s).'.center(MAX_WIDTH))
        print(f'Scores: {self.p1.name} = {self.p1.scores},  '
              f'{self.p2.name} = {self.p2.scores},  '
              f'Ties: {ties}'.center(MAX_WIDTH))
        if self.p1.scores > self.p2.scores:
            print(f'{self.p1.name} wins this '
                  f'game!'.upper().center(MAX_WIDTH))
        elif self.p1.scores < self.p2.scores:
            print(f'{self.p2.name} wins this '
                  f'game!'.upper().center(MAX_WIDTH))
        else:
            print('It is a tie game!'.upper().center(MAX_WIDTH))
        print_wait('*'*MAX_WIDTH)

    def print_go(self):
        print(f"\n{'='*MAX_WIDTH}")
        print("Rock Paper Scissors, Go!")
        print_wait('=' * MAX_WIDTH)

    def print_player_moves(self):
        print(f'{self.p1.name} played {self.p1.last_move}')
        print_wait(f'{self.p2.name} played {self.p2.last_move}')

    def play_game(self):
        self.print_go()
        for _ in range(self.total_rounds):
            print(f'\nRound {self.rounds_count} {"-"*3}')
            self.play_round()
        self.print_game_over()

    def reset(self):
        self.p1.wins = False
        self.p2.wins = False
        if self.p1.last_move:
            self.p1.prev_move = self.p1.last_move
        if self.p2.last_move:
            self.p2.prev_move = self.p2.last_move
        self.p1.move()
        self.p2.move()
        self.p1.opp_last_move = self.p2.last_move
        self.p2.opp_last_move = self.p1.last_move

    def round_wins(self):
        if self.p1.last_move != self.p2.last_move:
            if self.beats():
                self.p1.wins = True
                self.p1.scores += 1
            else:
                self.p2.wins = True
                self.p2.scores += 1

    def play_round(self):
        self.reset()
        self.print_player_moves()
        self.round_wins()
        self.print_round_wins()
        self.rounds_count += 1

    def beats(self):
        return ((self.p1.last_move == 'rock' and
                 self.p2.last_move == 'scissors') or
                (self.p1.last_move == 'scissors' and
                 self.p2.last_move == 'paper') or
                (self.p1.last_move == 'paper' and
                 self.p2.last_move == 'rock'))

