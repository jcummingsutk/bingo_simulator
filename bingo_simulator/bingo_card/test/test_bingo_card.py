import pytest

from bingo_simulator.bingo_card.bingo_card import BingoCard
from bingo_simulator.bingo_card.bingo_card_generator import generate_bingo_card
from bingo_simulator.random_number_generator import SampleWithoutReplacement


def test_illegal_board():
    bad_board = [[1, 2], [2]]
    with pytest.raises(ValueError):
        BingoCard(bad_board)


def test_board_generator():
    number_generator = SampleWithoutReplacement(list(range(75)))
    expected_card_values = [
        [number_generator.sample_list[i] for i in range(3)],
        [number_generator.sample_list[i] for i in range(3, 6)],
        [number_generator.sample_list[i] for i in range(6, 9)],
    ]
    bingo_card = generate_bingo_card(3, 3, number_generator)
    assert expected_card_values == bingo_card.values
