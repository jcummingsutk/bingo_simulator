import unittest

import pytest

from bingo_simulator.bingo_card.bingo_card import BingoCard
from bingo_simulator.bingo_patterns import (
    create_corners_pattern,
    create_postage_pattern,
)


def test_corners_pattern():
    bingo_card_values = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    bingo_card = BingoCard(values=bingo_card_values)

    corners_pattern = create_corners_pattern(bingo_card=bingo_card)

    expected_pattern = [(0, 0), (1, 0), (0, 2), (1, 2)]

    unittest.TestCase().assertCountEqual(corners_pattern, expected_pattern)


def test_corners_pattern2():
    bingo_card_values = [
        [1, 2],
        [4, 5],
        [7, 8],
        [9, 10],
        [22, 25],
    ]
    bingo_card = BingoCard(values=bingo_card_values)

    corners_pattern = create_corners_pattern(bingo_card=bingo_card)

    expected_pattern = [(0, 0), (4, 0), (0, 1), (4, 1)]

    unittest.TestCase().assertCountEqual(corners_pattern, expected_pattern)


def test_corners_error_raised():
    bingo_card_values = [
        [1],
        [4],
        [7],
        [9],
        [22],
    ]
    bingo_card = BingoCard(values=bingo_card_values)
    with pytest.raises(ValueError):
        _ = create_corners_pattern(bingo_card=bingo_card)

    bingo_card_values = [[1, 2, 3, 4, 5]]
    bingo_card = BingoCard(values=bingo_card_values)
    with pytest.raises(ValueError):
        _ = create_corners_pattern(bingo_card=bingo_card)


def test_postage_pattern():
    bingo_card_values = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    bingo_card = BingoCard(values=bingo_card_values)

    corners_pattern = create_postage_pattern(bingo_card=bingo_card)

    expected_pattern = [(1, 2), (1, 1), (0, 2), (0, 1)]

    unittest.TestCase().assertCountEqual(corners_pattern, expected_pattern)


def test_postage_pattern2():
    bingo_card_values = [
        [1, 2],
        [4, 5],
        [7, 8],
        [9, 10],
        [22, 25],
    ]
    bingo_card = BingoCard(values=bingo_card_values)

    postage_pattern = create_postage_pattern(bingo_card=bingo_card)

    expected_pattern = [(1, 1), (1, 0), (0, 1), (0, 0)]

    unittest.TestCase().assertCountEqual(postage_pattern, expected_pattern)
