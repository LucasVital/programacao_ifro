class Conta:
    __slots__ = [
        '_numero',
        '_titular',
        '_saldo',
        '_limite'
    ]

    def __init__(self, numero='', titular='', saldo=0.00, limite=0.00):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self.limite = limite

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = ''
        if not numero:
            raise Exception("Informe o número")
        self._numero = numero

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nome):
        self._titular = ''
        if len(nome) >= 5:
            self._titular = nome

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def deposita(self, valor):
        self._saldo += valor

    def saque(self, valor):
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
            if self._saldo < 0:
                self._limite = self._limite + self._saldo
                self._saldo = 0.00
            return True
        return False



