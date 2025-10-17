""" 
Calcular o Total de Compras empresa: JJK Lider Ltda

Nesta fase você deve criar um script 
que registre o preço de 5 produtos 
comprados por um cliente e calcule 
o valor total gasto.

Solicitações:
=============
O seu script deve solicitar ao usuário 
o preço de cada produto, um por vez.
É necessário usar um loop for para repetir 
o processo de entrada de preços.
Acumular o total dos preços em uma variável.
Exibir o valor total ao final.

Entrada:
========
Digite o preço do produto 1: ?
Digite o preço do produto 2: ?
Digite o preço do produto 3: ?
Digite o preço do produto 4: ?
Digite o preço do produto 5: ?

Saída:
======
O total gasto na compra foi: ?
 """
# Escreva seu código aqui



# 1o passo - entrada
total = 0

# 2o passo - For para coletar o preço dos 5 produtos
for produto_numero in range (1,6):
    produto_preco = float (input(f'Digite o preço do produto {produto_numero}: '))
    
    total += produto_preco

# 3o passo - saída
print(f'O total da sua compra foi: R${total: .2f}')











