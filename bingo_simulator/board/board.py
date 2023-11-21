from dataclasses import dataclass


@dataclass
class BingoCard:
    """Represents a rectangular bingo card which is a rectangular grid
    of height nrows, width ncols, and each rectangular cell has"""

    values: list[list[int]]

    def __post_init__(self):
        num_cols = self.ncols
        for row in self.values:
            if len(row) != num_cols:
                raise ValueError("Each row should have the same length")

    @property
    def nrows(self) -> int:
        return len(self.values)

    @property
    def ncols(self) -> int:
        return len(self.values[0])
