import random


class SampleWithoutReplacement:
    def __init__(self, sample_list: list[int]):
        self.sample_list = sample_list
        random.shuffle(self.sample_list)

    def generate(self) -> int:
        return self.sample_list.pop(0)
