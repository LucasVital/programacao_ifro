from classes import Conta

conta1 = Conta(numero='4040-6', titular="Lucas", limite=10000.00, saldo=0.45)

'''
conta1.saldo = 10000.00
conta1.tipo = 'conta corrente'
conta1.titular = 'Fulano de Tal'
'''

print(type(conta1))
print(dir(conta1))
print(conta1)

conta3 = Conta(numero='78-6', limite=1000, titular='Sabrina')
# conta3.limate = 3000
print(conta3.titular)

conta3.deposita(30)

print(conta3.saldo)

print(conta3.saque(4000))

print(conta3.saldo)
print(conta3.limite)
