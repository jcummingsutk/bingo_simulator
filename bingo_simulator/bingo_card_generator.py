from typing import Protocol

from bingo_simulator.bingo_card import BingoCard


class RandomNumberGenerator(Protocol):
    def generate(self) -> int:
        """"""


def generate_bingo_card(
    nrows: int, ncols: int, random_number_generator: RandomNumberGenerator
) -> BingoCard:
    """Generates the values of a square bingo card with nrows and ncols using the
    specified random number generator, then resets the random number generator

    Args:
        nrows (int): number of rows in the bingo card
        ncols (int): number of columns in the bingo card
        random_number_generator (RandomNumberGenerator): random number generator that
        makes the values in the bingo card slots

    Returns:
        BingoCard: generated bingo card
    """
    values = []
    for row in range(nrows):
        row = [random_number_generator.generate() for _ in range(ncols)]
        values.append(row)
    random_number_generator.reset()
    return BingoCard(values)
