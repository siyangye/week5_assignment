import unittest
from main import Game, HumanPlayer


class TestLogic(unittest.TestCase):

    def test_game_get_winner(self):
        game = Game(HumanPlayer(), HumanPlayer());
        game.board = [
            [game.X_player, None, game.O_player],
            [None, game.X_player, None],
            [None, game.O_player, game.X_player],
        ]
        self.assertEqual(game.get_winner(), game.X_player)


if __name__ == '__main__':
    unittest.main()
