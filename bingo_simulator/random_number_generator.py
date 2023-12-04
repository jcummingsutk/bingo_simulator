import random


class SampleWithoutReplacement:
    """Generator that samples from a list without replacement by shuffling up a list
    and, on calling the generate function, retrieves the first item of the list
    """

    def __init__(self, sample_list: list[int]):
        """
        Args:
            sample_list (list[int]): the list of numbers that should be drawn from
        """
        self.sample_list = sample_list
        self.idx = 0
        random.shuffle(self.sample_list)

    def generate(self) -> int:
        """Returns the ith item of the shuffled list to simulate sampling without
        replacement

        Returns:
            int: random number
        """
        return_val = self.sample_list[self.idx]
        self.idx = self.idx + 1
        return return_val

    def reset(self):
        """Shuffles up the list and resets the index to 0."""
        self.idx = 0
        random.shuffle(self.sample_list)
