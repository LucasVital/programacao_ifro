from interface import FormasInterface


class Retangulo(FormasInterface):
    __slots__ = ('__base', '__altura')

    def __init__(self, base: int | float, altura: int | float) -> None:
        self.__base = base
        self.__altura = altura

    @property
    def base(self) -> int | float:
        return self.__base

    @base.setter
    def base(self, base) -> None:
        self.__base = base

    @property
    def altura(self) -> int | float:
        return self.__altura

    @altura.setter
    def altura(self, altura) -> None:
        self.__altura = altura

    def get_area(self) -> int | float:
        area = self.__base * self.__altura
        return area

    def get_perimetro(self) -> int | float:
        perimetro = (2 * self.__base) + (2 * self.__altura)
        return perimetro
