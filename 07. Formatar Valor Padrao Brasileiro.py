
'''
Exemplo de entrada e saída:
===========================
Entrada: 1.000,00
Saída: O valor convertido para cálculo é: 1000.0

Detalhes adicionais:
====================
Esse processo de substituição é essencial para garantir que o Python 
interprete corretamente o valor, já que ele não reconhece automaticamente 
os separadores de milhar e decimal no formato brasileiro. 
Esse método é eficiente e pode ser utilizado sempre que você 
receber valores no formato 1.000,00.

Explicação:
==========
input(): Captura o valor digitado pelo usuário, que pode estar no formato 1.000,00 por exemplo.
1º replace('.', ''): Remove os pontos, que são usados no Brasil para separar os milhares.
2º replace(',', '.'): Substitui a vírgula por ponto, porque o Python usa ponto como separador decimal.
float(): Converte a string formatada para um número decimal(ponto flutuante), permitindo o uso em cálculos matemáticos.

'''

# 1o passo - Entradas
valor_input = input ('Digite o valor no formato brasileiro: (ex.:1.890,77)')


# 2o passo - remover os pontos (separadores de milhar) e substituir a vírgula
# por ponto ( separador de decimal )
# 1890.12
# transformar o valor para leitura do Python(padrão Americano 1890.12)

valor_formatado = valor_input.replace('.','').replace(',','.')

 
# 3o passo - converter para float
valor = float(valor_formatado) # 1890,77

# 4o passo - calcular 10% de desconto no valor informado
desconto = valor * 0.10

# 5o passo - calcular o valor finalc com o desconto
valor_final = valor - desconto

# 6o passo - exibir os resultados
print(f'Valor original: {valor}')
print(f'Desconto de 10%: {desconto}')
print(f'Valor final após desconto: {valor_final:.2f}')

































