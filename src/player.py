from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    player: str
