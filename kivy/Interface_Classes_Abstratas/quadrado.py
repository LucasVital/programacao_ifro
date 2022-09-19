from interface import FormasInterface


class Quadrado(FormasInterface):
    __slots__ = ('__lado')

    def __init__(self, lado: int | float) -> None:
        self.__lado = lado

    @property
    def lado(self) -> int | float:
        return self.__lado

    @lado.setter
    def lado(self, lado) -> None:
        self.__lado = lado

    def get_perimetro(self) -> int | float:
        perimetro = self.__lado * 4
        return perimetro

    def get_area(self) -> int | float:
        area = self.__lado * self.__lado
        return area
