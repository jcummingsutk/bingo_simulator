from typing import Protocol

from bingo_simulator.bingo_card.bingo_card import BingoCard


class RandomNumberGenerator(Protocol):
    def generate(self) -> int:
        """"""


def generate_bingo_card(
    nrows: int, ncols: int, random_number_generator: RandomNumberGenerator
) -> BingoCard:
    values = []
    for row in range(nrows):
        row = [random_number_generator.generate() for _ in ncols]
        values.append(row)
    return BingoCard(values)
