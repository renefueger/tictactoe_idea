from dataclasses import dataclass

from player import Player


class Players(list):

    @property
    def unique(self):
        return Players(set(self))
