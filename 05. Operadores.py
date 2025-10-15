"""
    SISTEMA DE VENDAS.
        Nesta etapa vamos lidar apenas com o 
        cadastro do produto.

    CRIE AS VARIÁVEIS DE ## ENTRADA ##
        Nome do produto. 
        Preço sem desconto
        Porcentagem de desconto

    ## PROCESSAMENTO ##
        Calcule o novo preço do produto com desconto

    VARIÁVEIS DE ## SAÍDA ##
        Nome do produto.
        Preço com desconto.
"""

# Bibliotecas do Python:
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

#Escreva seu código abaixo

# 1o passo - Entradas - variáveis
nome_produto = input('Nome do Produto')
preco = float (input('Preço sem desconto'))
desconto = float(input('Percentual de desconto(%): ')) # 9.5
produto_estoque = True #Verdadeiro(boleano)

# 2o passo - Processamento
valor_desconto = preco * desconto / 100
preco_com_desconto = preco - valor_desconto


# 3o passo - Saídas / Resultados
print ('/n Resumo do Produto')
print(f'Nome: {nome_produto}')
print (f'Preço com desconto: {preco_com_desconto: .2f}') #2894.77

#4o passo - validar produto_estoque
if produto_estoque == True:
    print('Produto no estoque')
else: # senão
    print('Produto fora do estoque')













