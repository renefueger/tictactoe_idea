from dataclasses import dataclass

from field import Field


@dataclass
class UnoccupiedField(Field):
    @property
    def player(self):
        return None
