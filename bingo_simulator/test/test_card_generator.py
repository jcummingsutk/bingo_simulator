from bingo_simulator.bingo_card_generator import generate_bingo_card


class IncrementingNumberGeneratorTest:
    def __init__(self, start_value: int):
        self.value = start_value

    def generate(self) -> int:
        return_value = self.value
        self.value = self.value + 1
        return return_value


def test_card_generator():
    number_generator = IncrementingNumberGeneratorTest(3)
    nrows = 2
    ncols = 4
    bingo_card = generate_bingo_card(
        nrows=nrows, ncols=ncols, random_number_generator=number_generator
    )
    assert bingo_card.nrows == nrows
    assert bingo_card.ncols == ncols

    expected_result = [[3, 4, 5, 6], [7, 8, 9, 10]]
    assert expected_result == bingo_card.values
