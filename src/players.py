from dataclasses import dataclass

from player import Player


@dataclass
class Players:
    _players: [Player]

    def __iter__(self):
        yield from self._players

    def __len__(self):
        return len(self._players)

    @property
    def unique(self):
        return Players(set(self._players))