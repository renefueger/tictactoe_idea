from board import Board
from game import Game


class Rule:
    def apply(self, original_game: Game, board: Board) -> Game:
        raise NotImplementedError
