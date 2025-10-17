# Bibliotecas do Python:
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

# ************ BIBLIOTECA IF **************

# >>>>> https://docs.python.org/3/tutorial/controlflow.html#if-statements <<<<<<

# *****************************************

'''
    Resumo: tomar decisões lógicas com base em diferentes cenários

    Tabela - Operadores Relacionais

            == Igual a
            != Diferente
            >= Maior ou igual
            >	Maior que
            <	Menor que
            <= Maior ou igual

    Operadores Lógicos

            or OU lógico
            and E lógico

'''


# ----------------------------------------------
#           Condição simples: if... else...
# -----------------------------------------------

'''
    Para compreender melhor o conceito de verificação
    com (if...else...), vamos analisar o cenário a seguir:

    ENTRADAS
    ========
        salario recebido = variável para receber valor monetário
        total de gastos = variável para receber valor monetário
    
    VERIFICAÇÃO
    ===========
        se o salário recebido for maior ou igual ao total de gatos então,
        mostre a mensagem 'Gastos dentro do Orçamento!'
        senão, mostre a mensagem 'Orçamento estourado!'    
'''
# Escreva seu código aqui

# 1o passo - Entradas - variáveis
salario_recebido = float (input('Digite o seu salário: '))
total_gastos = float (input('Qual é o total de gastos: '))


# 2o passo - Condições/Verificações

if salario_recebido >= total_gastos: 
    print (f'Seu salário é: {salario_recebido: .2f}. Gastos de{total_gastos: .2f} dentro do orçamento! Saldo:{round (salario_recebido - total_gastos, 2)}')
else:
    print (f'Orçamento estourado!! Déficit: {round (salario_recebido - total_gastos, 2)}')






































































































































