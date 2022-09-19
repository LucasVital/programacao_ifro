import abc
class FormaGeometrica(abc.ABC):
    
    @abc.abstractmethod
    def calcular_perimetro(self, *args):
        pass

    
    @abc.abstractmethod
    def calcular_area(self, *args):
        pass