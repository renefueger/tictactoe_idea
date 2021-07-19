from columns import Columns
from diagonals import Diagonals
from fields import Fields
from rows import Rows


class Board:
    def __init__(self, board_representation: Fields = None):
        self._fields = board_representation

        self.rows = Rows.create(board_representation)
        self.columns = Columns.create(board_representation)
        self.diagonals = Diagonals.create(board_representation)

    @property
    def fields(self) -> Fields:
        return self._fields;

    @property
    def occupied_fields(self) -> Fields:
        return self._fields.occupied
