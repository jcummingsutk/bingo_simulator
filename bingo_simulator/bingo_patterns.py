from enum import Enum

from bingo_simulator.bingo_card import BingoCard


class StandardBingoPatternName(str, Enum):
    POSTAGE_STAMP = "postage stamp"
    CORNERS = "corners"


def create_postage_pattern(bingo_card: BingoCard) -> list[tuple[int, int]]:
    """Creates a list of tuples representing the postage stamp pattern,
    which is the 4 spots in the upper right hand corner of the card.

    Example: if the card is [[1, 2, 3], [4, 5, 6]], so that there are 2 rows
    and 3 columns, then the postage stamp pattern would be the coordinates
    [(0, 1), (0, 2), (1, 1), (1, 2)].

    Visulized with xs marking a location of the
    pattern and Os with blank spots::
    O O O O O ... O X X
    O O O O O ... O X X
    O O O O O ... O O O
    .    .
    .      .
    .        .    O O O
    O O O O O ... O O O

    Args:
        bingo_card (BingoCard): Card for which to make the bingo pattern

    Raises:
        ValueError: Raised if there are not enough rows/columns to make a bingo pattern

    Returns:
        list[tuple[int, int]]: List of coordinates for the postage pattern
    """
    if bingo_card.nrows < 2 or bingo_card.ncols < 2:
        raise ValueError("Bingo Card not large enough")
    return [
        (0, bingo_card.ncols - 1),
        (1, bingo_card.ncols - 1),
        (0, bingo_card.ncols - 2),
        (1, bingo_card.ncols - 2),
    ]


def create_corners_pattern(bingo_card: BingoCard) -> list[tuple[int, int]]:
    """Creates a list of coordinates representing the four corners of the bingo card.

    Example: [[1, 2, 3], [4, 5, 6]], response is [(0, 0), (0, 2), (0, 1), (1, 2)]

    Visualized:
    X O O O O ... O O X
    O O O O O ... O O O
    O O O O O ... O O O
    .    .
    .      .
    .        .    O O O
    X O O O O ... O O X

    Args:
        bingo_card (BingoCard): Card to make the corners pattern for

    Raises:
        ValueError: raised if there are not enough rows and columns to make the pattern

    Returns:
        list[tuple[int, int]]: list of coordinates for the pattern
    """
    if bingo_card.nrows < 2 or bingo_card.ncols < 2:
        raise ValueError("Bingo Card not large enough")
    return [
        (0, 0),
        (0, bingo_card.ncols - 1),
        (bingo_card.nrows - 1, 0),
        (bingo_card.nrows - 1, bingo_card.ncols - 1),
    ]
