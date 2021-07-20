from __future__ import annotations

from dataclasses import dataclass
from typing import Collection

from fields import Fields
from row import Row


@dataclass
class Rows:
    _rows: Collection[Row]

    def __iter__(self):
        yield from self._rows

    @staticmethod
    def create(board_representation: Fields) -> Rows:
        return Rows(list(map(lambda row_number: Row.create(board_representation, row_number), range(3))))
