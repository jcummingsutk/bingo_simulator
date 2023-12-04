from enum import Enum

from bingo_simulator.bingo_card.bingo_card import BingoCard


class StandardBingoPatternName(str, Enum):
    POSTAGE_STAMP = "postage stamp"
    CORNERS = "corners"


def create_postage_pattern(bingo_card: BingoCard) -> list[tuple[int, int]]:
    if bingo_card.nrows < 2 or bingo_card.ncols < 2:
        raise ValueError("Bingo Card not large enough")
    return [
        (0, bingo_card.ncols - 1),
        (1, bingo_card.ncols - 1),
        (0, bingo_card.ncols - 2),
        (1, bingo_card.ncols - 2),
    ]


def create_corners_pattern(bingo_card: BingoCard) -> list[tuple[int, int]]:
    if bingo_card.nrows < 2 or bingo_card.ncols < 2:
        raise ValueError("Bingo Card not large enough")
    return [
        (0, 0),
        (0, bingo_card.ncols - 1),
        (bingo_card.nrows - 1, 0),
        (bingo_card.nrows - 1, bingo_card.ncols - 1),
    ]
