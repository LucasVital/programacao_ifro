from inspect import ArgSpec
from interface import FormaGeometrica

class Quadrilatero(FormaGeometrica):
    def __init__(self, l1, l2, l3, l4) -> None:
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.perimetro = 0

    def calcular_perimetro(self, *args):
        for l in args:
            self.perimetro += l


