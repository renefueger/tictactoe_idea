from dataclasses import dataclass

from columns import Columns
from diagonals import Diagonals
from fields import Fields
from rows import Rows


@dataclass
class Board:
    fields: Fields

    @property
    def occupied_fields(self) -> Fields:
        return self.fields.occupied

    @property
    def rows(self) -> Rows:
        return Rows.create(self.fields)

    @property
    def columns(self) -> Columns:
        return Columns.create(self.fields)

    @property
    def diagonals(self) -> Diagonals:
        return Diagonals.create(self.fields)
