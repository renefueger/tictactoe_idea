from dataclasses import dataclass

from fields import Fields
from row import Row


@dataclass
class Rows:
    _rows: [Row]

    def __iter__(self):
        yield from self._rows

    @staticmethod
    def create(board_representation: Fields):
        return Rows(list(map(lambda row_number: Row.create(board_representation, row_number), range(3))))


