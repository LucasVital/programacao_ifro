class Conta:

    def __init__(self, numero, titular, limite, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            if self.saldo < 0:
                self.limite = self.limite + self.saldo
                self.saldo = 0.00
            return True
        return False



