import pytest

from board_creator import BoardCreator
from finished_game import FinishedGame
from is_board_full_rule import IsBoardFullRule
from player_occupies_column_rule import PlayerOccupiesColumnRule
from player_occupies_diagonal_rule import PlayerOccupiesDiagonalRule
from player_occupies_row_rule import PlayerOccupiesRowRule
from rules import Rules
from running_game import RunningGame


class TestTicTacToe:
    def setup_method(self, method):
        rules = Rules([IsBoardFullRule(),
                       PlayerOccupiesRowRule(),
                       PlayerOccupiesColumnRule(),
                       PlayerOccupiesDiagonalRule(),
                       ])
        self.game = RunningGame(rules)

    def test_running_game_applying_rules_on_empty_board_returns_running_game(self):
        board = BoardCreator.create([
            '___',
            '___',
            '___'
        ])
        assert isinstance(self.game.apply_rules(board), RunningGame)

    @pytest.mark.parametrize('rows', [['___',
                                       '_xo',
                                       '_x_'
                                       ],
                                      ['_x_',
                                       '_xo',
                                       '___'
                                       ]
                                      ])
    def test_running_game_applying_rules_on_not_finished_board_returns_running_game(self, rows):
        board = BoardCreator.create(rows)
        assert isinstance(self.game.apply_rules(board), RunningGame)

    def test_running_game_applying_rules_on_full_board_returns_finished_game(self):
        board = BoardCreator.create([
            'oxo',
            'xox',
            'xox'
        ])
        assert isinstance(self.game.apply_rules(board), FinishedGame)

    @pytest.mark.parametrize('rows', [['___',
                                       'xxx',
                                       '___'],
                                      ['ooo',
                                       '___',
                                       '___'],
                                      ['___',
                                       '___',
                                       'xxx']])
    def test_running_game_applying_rules_on_row_board_returns_finished_game(self, rows):
        board = BoardCreator.create(rows)
        assert isinstance(self.game.apply_rules(board), FinishedGame)

    @pytest.mark.parametrize('rows', [['_x_',
                                       '_x_',
                                       '_x_'],
                                      ['x__',
                                       'x__',
                                       'x__'],
                                      ['__o',
                                       '__o',
                                       '__o']])
    def test_running_game_applying_rules_on_column_board_returns_finished_game(self, rows):
        board = BoardCreator.create(rows)
        assert isinstance(self.game.apply_rules(board), FinishedGame)

    def test_running_game_applying_rules_on_diagonal1_board_returns_finished_game(self):
        board = BoardCreator.create([
            'x__',
            '_x_',
            '__x'
        ])
        assert isinstance(self.game.apply_rules(board), FinishedGame)

    def test_running_game_applying_rules_on_diagonal2_board_returns_finished_game(self):
        board = BoardCreator.create([
            '__x',
            '_x_',
            'x__'
        ])
        assert isinstance(self.game.apply_rules(board), FinishedGame)
