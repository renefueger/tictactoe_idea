from board import Board
from finished_game import FinishedGame
from game import Game
from rule import Rule


class IsBoardFullRule(Rule):
    def apply(self, original_game: Game, board: Board) -> Game:
        if board.fields == board.occupied_fields:
            return FinishedGame()
        return original_game
