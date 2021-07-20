from __future__ import annotations
from dataclasses import dataclass
from typing import List, Collection

from diagonal import Diagonal
from fields import Fields


@dataclass
class Diagonals:
    _diagonals: Collection[Diagonal]

    def __iter__(self):
        yield from self._diagonals

    @staticmethod
    def create(board_representation: Fields) -> Diagonals:
        return Diagonals([
            Diagonal.from_top_left_to_bottom_right(board_representation),
            Diagonal.from_bottom_left_to_top_right(board_representation)
        ])
