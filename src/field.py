from dataclasses import dataclass

from position import Position


@dataclass
class Field:
    _position: Position

    @property
    def position(self) -> Position:
        return self._position
