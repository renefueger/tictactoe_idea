from __future__ import annotations

from dataclasses import dataclass
from typing import Collection

from player import Player


@dataclass
class Players:
    _players: Collection[Player]

    def __iter__(self):
        yield from self._players

    def __len__(self):
        return len(self._players)

    @property
    def unique(self) -> Players:
        return Players(set(self._players))
