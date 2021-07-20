from typing import Collection

from board import Board
from game import Game
from rule import Rule


class Rules:
    def __init__(self, rules: Collection[Rule]):
        self.rules = rules

    def apply(self, game: Game, board: Board) -> Game:
        games_after_applying_rule = list(map(lambda rule: rule.apply(game, board), self.rules))
        different_games_from_original = filter(lambda rule_applied_game: rule_applied_game != game,
                                               games_after_applying_rule)
        return next(different_games_from_original, game)
