from retangulo import Retangulo
from quadrado import Quadrado
from circulo import Circulo


while True:
    try:
        quantidade_formas = int(input('Quantas formas deseja criar? '))
        break
    except (ValueError, TypeError, KeyboardInterrupt):
        print(
            '\033[31mERRO: Por favor, digite um número inteiro.\033[m')
        continue

vetor = []

while quantidade_formas > len(vetor):

    for f in range(quantidade_formas):

        print('1 - Retangulo')
        print('2 - Quadrado')
        print('3 - Circulo')

        while True:
            try:
                forma = int(input('Digite o número da forma [1, 2 ou 3]: '))
                break
            except (ValueError, TypeError, KeyboardInterrupt):
                print(
                    '\033[31mERRO: Por favor, digite um número válido [1, 2 ou 3].\033[m')
                continue

        if forma == 1:
            while True:
                try:
                    base = float(input('informe a base: '))
                    altura = float(input('informe a altura: '))
                    vetor.append(Retangulo(base, altura))
                    break
                except (ValueError, TypeError, KeyboardInterrupt):
                    print(
                        '\033[31mERRO: Por favor, digite um número válido.\033[m')
                    continue
        if forma == 2:
            while True:
                try:
                    lado = float(input('informe o lado: '))
                    vetor.append(Quadrado(lado))
                    break
                except (ValueError, TypeError, KeyboardInterrupt):
                    print(
                        '\033[31mERRO: Por favor, digite um número válido.\033[m')
                    continue
        if forma == 3:
            while True:
                try:
                    raio = float(input('informe o raio: '))
                    vetor.append(Circulo(raio))
                    break
                except (ValueError, TypeError, KeyboardInterrupt):
                    print(
                        '\033[31mERRO: Por favor, digite um número válido.\033[m')
                    continue


print()

for obj in vetor:
    if isinstance(obj, Retangulo):
        print(
            f'Retangulo: base={obj.base}, altura={obj.altura}, Perimetro:{obj.get_perimetro():.2f}, Area:{obj.get_area()}')
    if isinstance(obj, Quadrado):
        print(
            f'Quadrado: lado={obj.lado}, Perimetro:{obj.get_perimetro():.2f}, Area:{obj.get_area()}')
    if isinstance(obj, Circulo):
        print(
            f'Circulo: raio={obj.raio}, Perimetro:{obj.get_perimetro():.2f}, Area:{obj.get_area()}')
