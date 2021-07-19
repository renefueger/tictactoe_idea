from board import Board
from game import Game
from rules import Rules


class RunningGame(Game):
    def __init__(self, rules: Rules):
        self.rules = rules

    def apply_rules(self, board: Board) -> Game:
        return self.rules.apply(self, board)
