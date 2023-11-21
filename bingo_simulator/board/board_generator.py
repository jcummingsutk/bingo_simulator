from typing import Protocol, Union


class RandomNumberGenerator(Protocol):
    def generate(self) -> Union[float, int]:
        """"""
