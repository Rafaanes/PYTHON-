'''
Onde usar tupla no mundo profissional?
======================================
Situação Profissional	    Por que usar tupla?
---------------------       -------------------
Cadastro de funcionários	Dados fixos e protegidos contra alterações
Agenda de reuniões	        Reuniões com data, hora e participantes imutáveis
Controle de produtos	    Informações de produto que não mudam (nome, código, preço)
Coordenadas geográficas	    Latitude e longitude são fixas
Configurações de sistema	Parâmetros que não devem ser alterados durante execução

'''

'''
Enunciado: Cadastro de Produto
===============================

Você trabalha em uma empresa e precisa registrar os dados de um produto:

    - Nome do produto

    - Código do produto

    - Preço

    - Quantidade em estoque

Esses dados não devem ser alterados acidentalmente.

'''

# 1o PASSO - antes (usando lista  - menos seguro)
# cadastro de produto usando lista
# problema: os dados podem ser alterados sem querer
produto = ['Notebook Dell', 1001, 3499.90, 25]


# alguém altera o nome do produto por engano
produto[0] = 'Notebook HP'


# exibindo os dados
print('Produto (com lista):')
print(f'Nome: {produto[0]}')
print(f'Código: {produto[1]}')
print(f'Preço: {produto[2]}')
print(f'Estoque: {produto[3]} unidades')


# 2o PASSO - TUPLA 
# usando (tupla - mais seguro)
# cadastro de produto usando tupla
# vantagem: os dados estão protegidos contra alterações
produto = ('Notebook Dell', 1001, 3499.90, 25)

# ao tentar alterar o 1º produto (vai dar ERRO)
# produto[0] = 'Notebook HP' # isso não é permitido com TUPLA !

print('\nProduto (com TUPLA):')
print(f'Nome: {produto[0]}')
print(f'Código: {produto[1]}')
print(f'Preço: {produto[2]}')
print(f'Estoque: {produto[3]} unidades')

