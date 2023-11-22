from dataclasses import dataclass

from bingo_simulator.bingo_card.bingo_card import BingoCard


@dataclass
class BingoGame:
    bingo_card: BingoCard
    bingo_pattern: list[tuple[int, int]]
    drawn_values: list[int]

    def __post_init__(self):
        self.check_pattern_validity()

    def check_pattern_validity(self):
        raise NotImplementedError

    def check_winner(self) -> bool:
        raise NotImplementedError
