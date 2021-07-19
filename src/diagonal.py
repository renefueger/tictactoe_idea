from dataclasses import dataclass

from field_container import FieldContainer
from fields import Fields
from position import Position


@dataclass
class Diagonal(FieldContainer):
    @classmethod
    def from_top_left_to_bottom_right(cls, board_representation: Fields):
        return Diagonal(board_representation.with_positions([Position(0, 0), Position(1, 1), Position(2, 2)]))

    @classmethod
    def from_bottom_left_to_top_right(cls, board_representation: Fields):
        return Diagonal(board_representation.with_positions([Position(0, 2), Position(1, 1), Position(2, 0)]))
