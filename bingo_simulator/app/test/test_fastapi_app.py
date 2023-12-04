import unittest

from fastapi.testclient import TestClient

from bingo_simulator.app.main import app
from bingo_simulator.bingo_card import BingoCard

client = TestClient(app)


def test_dummy_route():
    response = client.get("/test")
    assert response.json() == {"test": "data_new_updating_with_ci"}


def test_bingo_card():
    min_val = 0
    max_val = 300
    num_rows = 5
    num_cols = 6
    response = client.get(
        f"/bingo_card?min_card_value={min_val}&max_card_value={max_val}&num_rows={num_rows}&num_cols={num_cols}"
    )
    values = response.json()["values"]
    card = BingoCard(values)
    assert card.ncols == 6
    assert card.nrows == 5

    for row in card.values:
        for val in row:
            assert val >= min_val
            assert val <= max_val


def test_check_game():
    bingo_card_values = [[1, 2, 3], [4, 5, 6]]
    bingo_pattern = [(0, 1), (0, 2)]
    drawn_values = [11, 2, 3, 5]
    response = client.post(
        "/check_game",
        json={
            "card": {"values": bingo_card_values},
            "pattern": bingo_pattern,
            "drawn_values": drawn_values,
        },
    )
    assert response.json() == {"game_won": True}

    bingo_card_values = [[1, 2, 3], [4, 5, 6]]
    bingo_pattern = [(0, 1), (0, 2)]
    drawn_values = [11, 2, 5]
    response = client.post(
        "/check_game",
        json={
            "card": {"values": bingo_card_values},
            "pattern": bingo_pattern,
            "drawn_values": drawn_values,
        },
    )
    assert response.json() == {"game_won": False}


def test_get_postage_stamp():
    bingo_card_values = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    response = client.post(
        r"/bingo_pattern/postage%20stamp",
        json={
            "values": bingo_card_values,
        },
    )
    returned_pattern = response.json()["pattern"]
    expected_pattern = [[0, 2], [1, 2], [0, 1], [1, 1]]

    unittest.TestCase().assertCountEqual(returned_pattern, expected_pattern)


def test_get_corners():
    bingo_card_values = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    response = client.post(
        r"/bingo_pattern/corners",
        json={
            "values": bingo_card_values,
        },
    )
    returned_pattern = response.json()["pattern"]

    expected_pattern = [[0, 0], [0, 2], [1, 0], [1, 2]]

    unittest.TestCase().assertCountEqual(returned_pattern, expected_pattern)
