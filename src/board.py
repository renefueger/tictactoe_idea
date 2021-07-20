from columns import Columns
from diagonals import Diagonals
from fields import Fields
from rows import Rows
from typing import Optional


class Board:
    def __init__(self, board_representation: Fields):
        self._fields = board_representation

        self.rows = Rows.create(board_representation)
        self.columns = Columns.create(board_representation)
        self.diagonals = Diagonals.create(board_representation)

        # TODO: board_representation now duplicated 4 times?

    @property
    def fields(self) -> Optional[Fields]:
        return self._fields

    @property
    def occupied_fields(self) -> Optional[Fields]:
        if not self._fields:
            return None
        return self._fields.occupied
