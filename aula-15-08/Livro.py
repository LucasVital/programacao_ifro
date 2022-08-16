class Livro:
    __slots__ = [
        '_titulo',
        '_autor',
        '_paginas',
        '_preco',
    ]

    def __init__(self, titulo=None, autor=None, paginas=None, preco=None):
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas
        self._preco = preco

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        if not titulo:
            raise Exception('Informe o título.')
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        if not autor:
            raise Exception('Informe o nome do autor.')
        self._autor = autor

    @property
    def paginas(self):
        return self._paginas

    @paginas.setter
    def paginas(self, paginas):
        if not paginas:
            raise Exception('Informe o número de páginas.')
        self._paginas = paginas

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        if not preco:
            raise Exception('Informe o preço do livro.')
        elif preco < 0:
            raise Exception('O preço não pode ser negativo.')
        self._preco = preco
