from dataclasses import dataclass

from bingo_simulator.bingo_card.bingo_card import BingoCard


@dataclass
class BingoGame:
    """Represents a bingo game. Contains a bingo cardwith a 2d array of values to
    match, a pattern specifying which spots on the bingo card need to match to win, and
    the values which have been randomly drawn.
    """

    bingo_card: BingoCard
    bingo_pattern: list[tuple[int, int]]
    drawn_values: list[int]

    def __post_init__(self):
        self.check_pattern_validity()

    def check_pattern_validity(self):
        """Checks that the bingo pattern is consistent with the bingo board. Each
        coordinate in the pattern should be within the number of rows and columns of
        the rectangular bingo board
        """
        max_row_in_card = self.bingo_card.nrows
        max_col_in_card = self.bingo_card.ncols
        for row, col in self.bingo_pattern:
            if row not in range(max_row_in_card):
                raise ValueError(
                    f"Pattern is not compatible with the bingo card. Row \
number {row} is out of bounds of the number of valid rows {0, max_row_in_card}"
                )
            if col not in range(max_col_in_card):
                raise ValueError(
                    f"Pattern is not compatible with the bingo card. Column \
number {col} is out of bounds of the total number of valid columns {0, max_col_in_card}"
                )

    def check_winner(self) -> bool:
        raise NotImplementedError
