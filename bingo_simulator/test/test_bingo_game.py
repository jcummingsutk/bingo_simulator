import pytest

from bingo_simulator.bingo_card.bingo_card import BingoCard
from bingo_simulator.bingo_game import BingoGame


def test_invalid_games():
    bingo_card_values = [[1, 2, 3], [2, 3, 4]]
    card = BingoCard(bingo_card_values, each_value_unique=False)
    # invalid pattern bleow, there are two tows, so the maximum row coordinate would
    # be 1
    pattern = [[0, 0], [2, 0]]
    with pytest.raises(ValueError):
        _ = BingoGame(bingo_card=card, bingo_pattern=pattern, drawn_values=[])

    # invalid pattern bleow, there are three columns, so the maximum row coordinate would
    # be 2
    bingo_card_values = [[1, 2, 3], [5, 6, 7], [8, 9, 10], [10, 11, 21]]
    card = BingoCard(bingo_card_values, each_value_unique=False)
    pattern = [[0, 0], [0, 3]]
    with pytest.raises(ValueError):
        _ = BingoGame(bingo_card=card, bingo_pattern=pattern, drawn_values=[])


def test_winners():
    bingo_card_values = [[1, 2, 3], [4, 5, 6]]
    bingo_card = BingoCard(values=bingo_card_values)
    bingo_pattern = [(0, 1), (0, 2)]
    drawn_values = [11, 2, 3, 5]
    bingo_game = BingoGame(
        bingo_card=bingo_card,
        bingo_pattern=bingo_pattern,
        drawn_values=drawn_values,
    )
    assert bingo_game.check_winner() is True

    bingo_card_values = [[1, 2, 5], [4, 8, 6]]
    bingo_card = BingoCard(values=bingo_card_values)
    bingo_pattern = [(0, 0), (0, 1)]
    drawn_values = [1, 2]
    bingo_game = BingoGame(
        bingo_card=bingo_card,
        bingo_pattern=bingo_pattern,
        drawn_values=drawn_values,
    )
    assert bingo_game.check_winner() is True


def test_losers():
    bingo_card_values = [[1, 2, 3], [4, 5, 6]]
    bingo_card = BingoCard(values=bingo_card_values)
    bingo_pattern = [(0, 0), (0, 2)]
    drawn_values = [11, 2, 3, 5]
    bingo_game = BingoGame(
        bingo_card=bingo_card,
        bingo_pattern=bingo_pattern,
        drawn_values=drawn_values,
    )
    assert bingo_game.check_winner() is False

    bingo_card_values = [[1, 2, 5], [4, 8, 6]]
    bingo_card = BingoCard(values=bingo_card_values)
    bingo_pattern = [(0, 0), (0, 1)]
    drawn_values = [1, 3]
    bingo_game = BingoGame(
        bingo_card=bingo_card,
        bingo_pattern=bingo_pattern,
        drawn_values=drawn_values,
    )
    assert bingo_game.check_winner() is False
