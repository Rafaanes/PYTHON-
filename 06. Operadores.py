"""
    SISTEMA DE VENDAS.
        Nesta etapa da vida, vamos lidar apenas 
        com o cadastro do produto.

    ENTRADA:
        Nome do produto. 
        Preço de custo.
        Percentual de lucro.
        Qtd vendida para análisar lucro.

    PROCESSAMENTO:
        Calcular o preço de venda com base no preço de 
        custo e no % de lucro

        Calcular e aplicar os seguintes impostos sobre 
        o preço de venda:

            ICMS: 18%
            PIS: 1.65%
            COFINS: 7.6%
            IPI: 10%

        Calcular o preço final do produto com impostos. 
        Calcular a margem de lucro percentual sobre o preço de venda.
        Calcular o lucro total vendendo 100 unidades do produto.

    SAÍDA:
        Nome do produto.
"""

# Bibliotecas do Python:
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

# Escreva seu código abaixo

# 1o passo - Entradas - variáveis e seus tipos de dados
nome_produto = input('Nome do produto: ').upper() #letras maiusculas
preco_custo = float(input('Preço de Custo: ')) # exemplo: 5895.45
percentual_de_lucro = float(input('Lucro(%): ')) # ex.: 8.5
qtde_vendida = int(input('Quantidade vendida minimo 100: '))

# 2o passo - Processamento - cálculos
preco_venda = preco_custo * (1 + percentual_de_lucro / 100)

# 3o passo - Atribuir os impostos as variáveis
percentual_icms = 18
percentual_pis = 1.65
percentual_cofins = 7.6
percentual_ipi = 10

# 4o passo - Calcular o preço final do produto com impostos
valor_icms = preco_venda * (percentual_icms/100)
valor_ipi = preco_venda * (percentual_ipi/100)
valor_pis = preco_venda * (percentual_pis/100)
valor_cofins = preco_venda * (percentual_cofins/100)

total_impostos = valor_icms + valor_pis + valor_cofins + valor_ipi

preco_final = preco_venda + total_impostos 

lucro_total = (preco_final - preco_custo - total_impostos) * qtde_vendida

margem_lucro_perecentual = lucro_total / (preco_venda * qtde_vendida)

receita_bruta = preco_final * qtde_vendida

receita_liquida = preco_venda * qtde_vendida

# 5o passo - Saídas (exibir os resultados)
print ('Resumo do Produto')
print(f'Nome do Produto: {nome_produto}')
print(f'Preço de custo: {preco_custo: .2f}')
print(f'Percentual e Lucro desejado: {percentual_de_lucro: .2f}')

print('\nCálculos de Preço e Impostos')
print(f'Preço de Vendas: {preco_venda: .2f}')

print('\nImpostos aplicados')
print(f'ICMS {percentual_icms} % valor R$ {valor_icms: .2f}')
print(f'COFINS {percentual_cofins} % valor R$ {valor_cofins: .2f}')
print(f'IPI {percentual_ipi} % valor R$ {valor_ipi: .2f}')
print(f'PIS {percentual_pis}% valor R$ {valor_pis: .2f}')

print(f'\nPreçofinal com impostos: R$ {preco_final: .2f}')
print(f'Lucro total vendendo: {qtde_vendida} unidade R$ {lucro_total: .2f}')

print(f'\nReceita Bruta: {receita_bruta: ,.2f}') # 590,789.77

print(f'Receita Líquida: {receita_liquida: ,.2f}') #ex. : 2,876,897.69




































