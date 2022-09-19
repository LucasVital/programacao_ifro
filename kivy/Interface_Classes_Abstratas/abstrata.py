from abc import ABC, abstractmethod


class Quadrilatero(ABC):
    __slots__ = ['__l1', '__l2', '__l3', '__l4']

    def __init__(self, l1, l2, l3, l4) -> None:
        self.__l1 = l1
        self.__l2 = l2
        self.__l3 = l3
        self.__l4 = l4
        self.perimetro = 0

    @abstractmethod
    def get_perimetro(self) -> None:
        self.perimetro = self.__l1 + self.__l2 + self.__l3 + self.__l4
        return self.perimetro
