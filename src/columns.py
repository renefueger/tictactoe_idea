from dataclasses import dataclass

from column import Column
from fields import Fields
from typing import Optional


@dataclass
class Columns:
    _columns: list[Column]

    def __iter__(self):
        yield from self._columns

    @staticmethod
    def create(board_representation: Fields):
        return Columns(list(map(lambda column_number: Column.create(board_representation, column_number), range(3))))
