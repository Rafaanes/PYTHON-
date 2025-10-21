'''

Cálculo de Comissão de Vendas
=============================

O sistema de comissão de vendas de uma empresa 
precisa calcular o valor a ser pago a um vendedor, 
com base no valor das vendas realizadas. 

A comissão do vendedor varia de acordo com a faixa de 
valor das vendas, conforme as regras abaixo:

Regras de Comissão:
===================

    Não atingiu a meta:
    ------------------- 
    - se o valor vendido menor ou igual a R$ 4.000,00, 
      a comissão será de 1% sobre o valor vendido.


    Atingiu a meta: 
    ---------------
    - se o valor vendido for maior do que R$ 4.000,00 e 
      menor ou igual a R$ 8.000,00 a comissão será de 
      5% sobre o valor vendido.

    Superou a meta: 
    ---------------
    - se o valor vendido for superior a R$ 8.000,00
      a comissão será de 10% sobre o valor vendido.


PEDE-SE
=======

1) O programa deve solicitar: 
    - nome do vendedor
    - valor total vendido

2) O valor da venda será informado no 
    formato brasileiro, com separador de milhar (ex: 1.500,00).

3) O sistema deve calcular a comissão do 
    vendedor com base nas faixas de vendas e 
    determinar o valor final a ser pago (valor vendido + comissão).

4) O valor final a ser pago deve ser exibido no 
    formato de moeda brasileira (ex: R$ 1.500,00).

5) exibir:
    nome do vendedor
    comissão aplicada
    valor das vendas
    valor total a ser pago ao vendedor      

'''

#Função
def calcular_total_vendido(recebe_valor,recebe_comissao):
    return recebe_valor + (recebe_valor * recebe_comissao)

def formatar_moeda(recebe_valor):
    texto = f'R$ {recebe_valor:_.2f}'
    return texto.replace('.',',').replace ('_','.')
    

### INICIO DO PROGRAMA ###

nome_vendedor = input ('Nome do vendedor: ').upper()
valor_vendido_input = float(input('Valor total vendido: '))

if valor_vendido_input <= 4000:
    comissao = 0.01
elif valor_vendido_input > 4000 and valor_vendido_input <=8000:
    comissao = 0.05      
else:
    comissao = 0.10
    
#calcular o valor total a receber, considerando a comissão.

valor_a_pagar = calcular_total_vendido(valor_vendido_input, comissao)

#resultados
print(f'Vendedor: {nome_vendedor}')
print(f'Comissão aplicada: {int(comissao * 100)}%')
print(f'Valor vendido: {formatar_moeda(valor_vendido_input)}')
print(f'Valor a receber: {formatar_moeda(valor_a_pagar)}')























































































