Exercícios
1. Identifique as classes com os seus atributos (classes de análise/domínio) para os
seguintes contextos:

a. Numa turma de um curso de graduação, temos disciplinas ministradas em salas
diferentes.

Curso
Graduação
Disciplinas
Salas


b. Está passando na rede de cinemas ArtFilme o filme “Jogos 2”, todos os dias, em três
sessões diárias. Aos sábados e domingos existem em algumas sessões duas salas de
exibição.

Cinema
Sala
Sessao
Filme
Data

2. Se dois desenvolvedores modelarem uma mesma classe X para sistemas distintos,
obrigatoriamente as classes terão os mesmos atributos e operações? Por que?
As classes e atributos mais basicos pode ter os mesmos nomes e atributor. Porem, 
outros atributos podem variar de acordo com a experiencia de cada desenvolvedor.

3. Identifique os atributos para as classes a seguir:
a. Conta-corrente
    - agência
    - número da conta
    - saldo
    - nome do titular

b. Caderno vendido em papelaria
    - fabricante
    - tipo_capa ( dura, mole)
    - tipo_caderno ( arame, brochura)
    - quantidade de folhas
    - quantidade de matéria

c. Arquivo de computador
    - nome do arquivo
    - data de criacao
    - data de modificação
    - extensão
    - tamanho
    - caminho

4. Analise os atributos a seguir e determine o nome da classe correspondente, no
contexto da informatização de uma clínica médica.
a. Classe: Medico
Atributos: nome, CRM, especialidade, data de admissão
Operações: Realizar Consulta, Prescrever Exame, Prescrever Receita
b. Classe: Consulta
Atributos: dia, hora, identificador de consulta paga, identificador de comparecimento
de cliente
Operações: Marcar, Desmarcar, Remarcar, Pagar Consulta, Registrar Comparecimento
do Paciente
c. Classe: Exame
Atributos: nome, tipo, instruções para realização, tempo de entrega
Operações: Listar Relação de Laboratórios Credenciados
d. Classe: Paciente
Atributos: nome, endereço, data de nascimento, sexo, histórico clínico
Operações: Lançar Dados da Consulta, Imprimir Histórico, Imprimir Ficha Médica,
Imprimir Exames Solicitados

5. Identifique nas classes adiante, que atributos e/ou operações não pertencem ao
escopo do problema.
a. Controle de alunos de ensino médio matriculados em um colégio.
Classe: Aluno
Atributos: nome, telefone, endereço, filiação, altura, data de nascimento, disciplina
Operações: Matricular, [Emitir Boleto], Obter Lista de Presença
b. Cadastro de professores de uma Universidade
Classe: Professor
Atributos: nome, formação acadêmica, data de nascimento, [data de casamento], sexo
Operações: Listar Disciplinas Habilitadas, [Emitir Contracheque],
c. Cadastro de livros de uma livraria
Classe: Livro
Atributos: título, ISBN, número de páginas, autores, editora, preço de custo, preço de
venda, ano de edição
Operações: Cadastrar Livro, Calcular Desconto Especial, [Imprimir Livro]


6. Defina uma superclasse que sirva para todas as subclasses de cada item a seguir:
a. Linha, Ponto, Polígono, Círculo
Vetorial
b. Creche, Escola de Nível Médio, Universidade, Curso de Idiomas
Instituicao
c. Aéreo, Fluvial, Terrestre
Transporte
d. Prefeito, Governador, Presidente
CargoExecutivo
