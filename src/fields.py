from dataclasses import dataclass

from field import Field
from occupied_field import OccupiedField
from player import Player
from players import Players
from position import Position
from unoccupied_field import UnoccupiedField


@dataclass
class Fields:
    _fields: [Field]

    def __iter__(self):
        yield from self._fields

    def __len__(self):
        return len(self._fields)

    @property
    def occupied(self):
        return Fields(self.of_type(OccupiedField))

    @property
    def unoccupied(self):
        return Fields(self.of_type(UnoccupiedField))

    def of_type(self, the_type: type):
        return list(filter(lambda field: isinstance(field, the_type), self._fields))

    def occupied_by(self, player: Player):
        return Fields(list(filter(lambda field: field.player == player, self._fields)))

    @property
    def players(self) -> Players:
        return Players(list(map(lambda field: field.player, self.occupied)))

    @property
    def unique_players(self) -> Players:
        return self.players.unique

    def with_row(self, row_number: int):
        return Fields(list(filter(lambda field: field.position.y == row_number, self._fields)))

    def with_column(self, column_number: int):
        return Fields(list(filter(lambda field: field.position.x == column_number, self._fields)))

    def with_positions(self, positions: [Position]):
        return Fields(list(filter(lambda field: field.position in positions, self._fields)))
