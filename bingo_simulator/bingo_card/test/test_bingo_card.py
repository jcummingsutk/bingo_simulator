import pytest

from bingo_simulator.bingo_card.bingo_card import BingoCard


def test_illegal_board():
    bad_board = [[1, 2], [2]]
    with pytest.raises(ValueError):
        BingoCard(bad_board)
