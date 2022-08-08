""""
Lucas Pedreira Vital
"""


# 12.Dada a função: y=5x+2y, determine os valores de y para x entre -10 a +10, onde x é inteiro



# 13.Escreva uma função chamada temDuplicata que tome uma lista e retorne True se houver
# algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.
def temDuplicata(lista):
    for n in lista:
        if lista.count(n) > 1:
            return True
    return False


lista = [1, 2, 3, 0, 4, 5, 6, 0]

print(temDuplicata(lista))


# 14.Escreva uma função que imprime todos os números primos entre 1 e 50
# Dica: um número é primo se ele for divisível apenas por 1 e ele mesmo, use o operador % (resto da divisão) para isso.
def primos(inicio, fim):
    for n in range(inicio, fim + 1):
        if n > 1:
            for p in range(2, n):
                if n % p == 0:
                    break
            else:
                print(n)


primos(1, 50)


# 15. Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra.
# Escreva uma função chamada e_anagrama que receba duas strings e retorne
# True se forem anagramas ou False caso contrário
def e_anagrama(palavra1, palavra2):
    if sorted(palavra1) == sorted(palavra2):
        return True
    else:
        return False


palavras = input('Digite duas palavras: ')
palavras = palavras.split()

print(e_anagrama(palavras[0], palavras[1]))
