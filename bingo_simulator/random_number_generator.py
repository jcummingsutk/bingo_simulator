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
        random.shuffle(self.sample_list)

    def generate(self) -> int:
        """Returns the first item of the shuffled list to simulate a random number
        bing drawn

        Returns:
            int: number from the list
        """
        return self.sample_list.pop(0)
