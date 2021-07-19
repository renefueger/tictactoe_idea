from finished_game import FinishedGame
from game import Game
from rule import Rule


class PlayerOccupiesRule(Rule):
    @classmethod
    def apply_for(cls, columns, original_game: Game) -> Game:
        rule_applies = map(lambda item: len(item.unique_players) == 1 and not any(item.unoccupied_fields), columns)
        if any(rule_applies):
            return FinishedGame()
        return original_game
