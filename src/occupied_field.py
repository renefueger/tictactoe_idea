from dataclasses import dataclass

from field import Field
from player import Player


@dataclass
class OccupiedField(Field):
    _player: Player

    @property
    def player(self) -> Player:
        return self._player;