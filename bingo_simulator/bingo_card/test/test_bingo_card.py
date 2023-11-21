import pytest

from bingo_simulator.board import BingoCard


def test_illegal_board():
    bad_board = [[1, 2], [2]]
    with pytest.raises(ValueError):
        BingoCard(bad_board)
