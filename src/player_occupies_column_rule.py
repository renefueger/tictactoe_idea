from board import Board
from game import Game
from player_occupies_rule import PlayerOccupiesRule


class PlayerOccupiesColumnRule(PlayerOccupiesRule):
    def apply(self, original_game: Game, board: Board) -> Game:
        return self.apply_for(board.columns, original_game)
