from Livro import Livro
from Data import Data

livro = Livro()
livro.titulo = 'Clean Code'
livro.autor = 'Robert C Martin'
livro.paginas = 432
livro.preco = 45.00

print('Livro: ', livro.titulo)
print('Autor:', livro.autor)
print('Páginas:', livro.paginas)
print('Preço: R$', livro.preco)


data = Data()
data.dia = '09'
data.mes = 10
data.ano = 1012


print(data.dia)
print(data.mes)
print(data.ano)
print(data.formatada())


