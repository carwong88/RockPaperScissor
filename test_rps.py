import unittest
import rps


class TestPaperScissorRock(unittest.TestCase):

    def test_beats_returns_true(self):
        p1 = rps.RandomPlayer()
        p2 = rps.RandomPlayer()
        game = rps.PaperScissorsRock(p1, p2)
        p1.last_move = 'rock'
        p2.last_move = 'scissors'
        assert game.beats() == True
        p1.last_move = 'scissors'
        p2.last_move = 'paper'
        assert game.beats() == True
        p1.last_move = 'paper'
        p2.last_move = 'rock'
        assert game.beats() == True

    def test_beats_returns_false(self):
        p1 = rps.RandomPlayer()
        p2 = rps.RandomPlayer()
        game = rps.PaperScissorsRock(p1, p2)
        p2.last_move = 'rock'
        p1.last_move = 'scissors'
        assert game.beats() == False
        p2.last_move = 'scissors'
        p1.last_move = 'paper'
        assert game.beats() == False
        p2.last_move = 'paper'
        p1.last_move = 'rock'
        assert not game.beats()

    def test_p1_wins(self):
        p1 = rps.RandomPlayer()
        p2 = rps.RandomPlayer()
        game = rps.PaperScissorsRock(p1, p2)
        game.p1.last_move = 'rock'
        game.p2.last_move = 'scissors'
        game.round_wins()

        assert p1.wins is True
        assert p1.scores == 1
        assert p2.wins is False
        assert p2.wins == 0

    def test_p2_wins(self):
        p1 = rps.RandomPlayer()
        p2 = rps.RandomPlayer()
        game = rps.PaperScissorsRock(p1, p2)
        game.p2.last_move = 'rock'
        game.p1.last_move = 'scissors'
        game.round_wins()

        assert p2.wins is True
        assert p2.scores == 1
        assert p1.wins is False
        assert p1.wins == 0