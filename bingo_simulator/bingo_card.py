from pydantic.dataclasses import dataclass


@dataclass
class BingoCard:
    """Represents a rectangular bingo card which is a rectangular grid
    of height nrows, width ncols, and each rectangular cell has"""

    values: list[list[int]]
    each_value_unique: bool = True

    def __post_init__(self):
        """Checks to make sure that the card is rectangular, each row having
        the same length, and that values are not repeated in the bingo card

        Raises:
            ValueError: raised if not rectangular
        """
        num_cols = self.ncols
        for row in self.values:
            if len(row) != num_cols:
                raise ValueError("Each row should have the same length")
        if self.each_value_unique:
            self.check_unique_values()

    def check_unique_values(self):
        """Ensures that each value in the card is unique

        Raises:
            ValueError: raised if there are duplicate values in the card
        """
        if not self.each_value_unique:
            return
        flat_values = [item for sublist in self.values for item in sublist]
        if len(flat_values) != len(set(flat_values)):
            raise ValueError("The bingo card should have unique values")

    @property
    def nrows(self) -> int:
        return len(self.values)

    @property
    def ncols(self) -> int:
        return len(self.values[0])
