from itertools import chain
from typing import Collection, Iterable

from board import Board
from field import Field
from fields import Fields
from occupied_field import OccupiedField
from player import Player
from position import Position
from unoccupied_field import UnoccupiedField


class BoardCreator:
    @classmethod
    def create_field(cls, row_number: int, column_number: int, value: str) -> Field:
        position = Position(column_number, row_number)
        if value == '_':
            return UnoccupiedField(position)
        return OccupiedField(position, Player(value))

    @classmethod
    def create_fields(cls, row_number: int, row: str) -> Iterable[Field]:
        return map(lambda arg: BoardCreator.create_field(row_number, arg[0], arg[1]), enumerate(row))

    @classmethod
    def create(cls, rows: Collection[str] = []) -> Board:
        single_fields = BoardCreator.flat_map_indexed(lambda arg: BoardCreator.create_fields(arg[0], arg[1]), rows)
        fields = Fields(single_fields)
        return Board(fields)

    @classmethod
    def flat_map_indexed(cls, function, rows) -> Collection[Field]:
        return list(chain.from_iterable(map(function, enumerate(rows))))
