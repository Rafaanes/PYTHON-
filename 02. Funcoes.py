'''
CENÁRIO
=======

Cálculo de Impostos com Desconto e Entrada de Produtos
------------------------------------------------------

Uma empresa deseja automatizar o processo de cálculo de 
impostos sobre produtos vendidos, considerando também 
eventuais descontos aplicados ao consumidor.

Pede-se crie um programa para:
-----------------------------

1) Solicite ao usuário quantos produtos deseja cadastrar.

2) Para cada produto, o usuário deve informar:

    Nome do produto

    Preço original (antes do desconto)

    Valor do desconto aplicado ao produto


3) O programa deve calcular:

    a) O valor dos impostos (IR, ISS, CSLL) com base no preço original

    b) IR (Imposto de Renda):

            20% para produtos com preço até R$ 2.000,00

            30% para produtos com preço acima de R$ 2.000,00

    c) ISS: 15% do preço original

    d) CSLL: 5% do preço original

    e) O preço final com desconto

4) Para cada produto, exibir:

    Nome do produto

    Preço original (formatado como moeda brasileira)

    Valor do desconto

    Preço final com desconto

    Valor total dos impostos calculados

'''


#2o passo - função 
#sempreque criar uma função, coloque no inicio do programa, caso contrário a função não será executada
#def = definir/criar

def calcular_imposto_total(recebe_valor):
    
    #calcular o IR
    
    if recebe_valor <= 2000:
        imposto_ir = 0.2 * recebe_valor 
    else:
        imposto_ir = 0.3 * recebe_valor
        
    imposto_iss = iss * recebe_valor
    imposto_csll = casll * recebe_valor
    total = imposto_ir + imposto_iss + imposto_csll
    
    return total


#3o passo - Função formatação
def formatar_moeda (recebe_valor):
    #usar '_' para facilitar a separação de milhar
    texto = f'R$ {recebe_valor:_.2f}'
    
    #converter para virgula decimal e ponto para milhar
    return texto.replace('.',',').replace('_','.')


## INICIO DO PROGRAMA ##

#1o passo - Variaveis - Entrada
iss = 0.15 #15%
casll = 0.05

#looping (for) que repete o processo para cada produto informado
qtd_produtos = int (input('Quantos produtos deseja cadastrar?'))

for numero_produto in range (qtd_produtos):
    print (f'Produto: {numero_produto +1}')
    
    #coletar os dados do produto
    nome_produto = input ('Digite o nome do produto: ')
    preco = preco = float (input('Digite o preço do produto: '))
    desconto = float (input('Digite o valor do desconto: '))/100
    
    #calculos (criar/ chamar a funçao)
    imposto_total = calcular_imposto_total (preco)
    
    preco_com_desconto = preco - (desconto * preco)

    #formatações
    texto_preco = formatar_moeda(preco)
    texto_preco_com_desconto = formatar_moeda(preco_com_desconto)
    texto_imposto_tot = formatar_moeda(imposto_total)
    
#resultados

    print(f'\nResumo do produto: {nome_produto}')
    print(f'Preço original: {texto_preco}')
    print(f'Desconto aplicado: {int(desconto*100)}%')
    print(f'Preço com desconto: {texto_preco_com_desconto}')
    print(f'Imposto total sobre preço original: {texto_imposto_tot}')




























































