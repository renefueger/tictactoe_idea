from __future__ import annotations
from dataclasses import dataclass

from field_container import FieldContainer
from fields import Fields


@dataclass
class Column(FieldContainer):
    @staticmethod
    def create(board_representation: Fields, column_number: int) -> Column:
        return Column(board_representation.with_column(column_number))
