from interface import FormasInterface


class Circulo(FormasInterface):
    __slots__ = ('__raio')

    def __init__(self, raio: int | float) -> None:
        self.raio = raio

    @property
    def raio(self) -> int | float:
        return self.__raio

    @raio.setter
    def raio(self, raio) -> None:
        self.__raio = raio

    def get_area(self) -> int | float:
        area = 3.14 * (self.__raio ** 2)
        return area

    def get_perimetro(self) -> int | float:
        perimetro = 2 * 3.14 * self.__raio
        return perimetro
