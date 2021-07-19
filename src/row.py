from dataclasses import dataclass

from field_container import FieldContainer
from fields import Fields


@dataclass
class Row(FieldContainer):
    @staticmethod
    def create(board_representation: Fields, row_number: int):
        return Row(board_representation.with_row(row_number))
