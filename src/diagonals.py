from dataclasses import dataclass

from diagonal import Diagonal
from fields import Fields


@dataclass
class Diagonals:
    _diagonals: [Diagonal]

    def __iter__(self):
        yield from self._diagonals

    @staticmethod
    def create(board_representation: Fields):
        return Diagonals([
            Diagonal.from_top_left_to_bottom_right(board_representation),
            Diagonal.from_bottom_left_to_top_right(board_representation)
        ])
