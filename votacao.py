"""
LUCAS PEDREIRA VITAL
"""
# Crie uma aplicação em python que receba os dados referentes a uma votação.
# O usuário informará deve informar se deseja ver os resultados ou se deseja votar.
# Caso deseje votar, o usuário deve informar o número do candidato à prefeito e o número do candidato à vereador.
# Os dados devem ser armazenados em um arquivo de texto.
# Caso o usuário deseje ver os resultados, o sistema chamará uma função que abre o arquivo para
# leitura e mostra o número do candidato e o percentual de votação que ele obteve até o momento.
# Separe os resultados em "Prefeito" e "Vereador".
import os


def lista_candidatos(candidatos):
    for v in range(0, len(candidatos)):
        print(f'{v + 1} - ', candidatos[v])

def criar_arquivo():
    if not os.path.isfile('votos_prefeito.txt'):
        with open('resultado.txt', 'w') as arquivo:
            arquivo.write('CANDIDATOS A PREFEITO:' + '\n')
            for x in range(0, len(canditados_prefeito)):
                arquivo.write(f'{canditados_prefeito[x]} = {round((votos_prefeitos[x] / total_votos_prefeito) * 100, 2)}% \n')

            arquivo.write('\n------------------------------------------------------------\n\n')
            arquivo.write('CANDIDATOS A VEREADORES:' + '\n')
            for x in range(0, len(canditados_vereador)):
                arquivo.write(f'{canditados_vereador[x]} = {round((votos_vereador[x] / total_votos_vereador) * 100, 2)}% \n')


canditados_prefeito = ['TETÉ DA SILVA', 'DUDO NETO']
votos_prefeitos = [0, 0]
canditados_vereador = ['ZÉ DO SITIO', 'PAULO PIMENTA', 'SERGIO LOCUTOR']
votos_vereador = [0, 0, 0]

total_votos_prefeito = 0
total_votos_vereador = 0



resposta = int(input(f'Escolha uma opção: {os.linesep}1 - INICIAR VOTACÃO {os.linesep}2 - RESULTADOS {os.linesep} opção: '))
continuar_votacao = 'S'

if resposta == 1:

    while continuar_votacao == 'S':

        print('VOTO PARA PREFEITO ')
        lista_candidatos(canditados_prefeito)

        voto_prefeito = int(input(f'Digite o número do canditado a prefeito: '))
        voto_prefeito -= 1
        try:
            votos_prefeitos[voto_prefeito] += 1
            total_votos_prefeito += 1
        except:
            print('Voto Nulo')

        print('*'*20)
        print('VOTO PARA VEREADOR')
        lista_candidatos(canditados_vereador)

        voto_vereador = int(input(f'Digite o número do canditado a vereador: '))
        voto_vereador -= 1
        try:
            votos_vereador[voto_vereador] += 1
            total_votos_vereador += 1
        except:
            print('Voto Nulo')

        continuar_votacao = input('Continuar votando? [s, n] | Resultado Parcial? [ r ]: ').upper()

    criar_arquivo()

if resposta == 2 or continuar_votacao == 'N':
    with open('resultado.txt', 'r') as arquivo:
        resultado = arquivo.readlines()
        for resultado in resultado:
            print(resultado)
