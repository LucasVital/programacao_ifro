class Data:
    __slots__ = ['__dia', '__mes', '__ano']

    def __init__(self, dia=None, mes=None, ano=None):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if int(dia) <= 0 or int(dia) > 31:
            raise Exception('Informe um dia válido.')
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes <= 0 or mes > 12:
            raise Exception('Informe um mês válido.')
        self.__mes = mes


    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if len(str(ano)) < 4 or len(str(ano)) > 4:
            raise Exception('Informe um ano válido.(2020)')
        self.__ano = ano

    def formatada(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
