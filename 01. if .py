
# Bibliotecas do Python:
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

# ************ BIBLIOTECA IF **************

# >>>>> https://docs.python.org/3/tutorial/controlflow.html#if-statements <<<<<<

# *****************************************
''' 
O if é uma estrutura condicional. Ele verifica se 
uma condição é verdadeira (True) e, 
se for, executa o código que está 
indentado logo abaixo dele.

Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Resumo: tomar decisões lógicas com base em diferentes cenários

    Tabela - Operadores Relacionais

            ==	Igual a
            !=	Diferente
            >=	Maior ou igual
            >	Maior que
            <	Menor que
            <=	Menor ou igual
    
    Operadores Lógicos

            or	OU lógico
            and	E lógico
            not	Negação


O if é uma estrutura condicional. Ele verifica se
uma condição é verdadeira (True) e, se for , executa o código
que está indentado logo abaixo dele.

    RESUMO
    ======
    if:(significa SE) verifica se uma condição é verdadeira.

    elif: (significa SENÃO SE) verifica outra condição, se a anterior for falsa.

    else: (significa SENAO) executa um bloco de código se todas as condições anteriores forem falsas.

'''
'''
    ESCOLA XYZ
    ==========

    ENTRADA ( variáveis )
    =======
    nota 1
    nota 2
    nota 3
    nota 4

    CÁLCULO
    =======
    media = (soma das notas) / por 4

    ANÁLISE
    =======
    se a media for maior ou igual a 7, 'Aprovado'

    se a media for menor do que 7, 'Reprovado'

'''

# Escreva seu código aqui

# 1o passo - declarar as variáveis - Entradas
nota1= float (input('Nota 1: '))
nota2= float (input('Nota 2: '))
nota3= float (input('Nota 3: '))
nota4= float (input('Nota 4: '))

# 2o passo - cálculos
media = (nota1 + nota2 + nota3 + nota4) / 4


# 3o passo - tomar a decisão com IF para saber se o aluno
# está: Aprovado ou Reprovado

if media >= 7:  
    print (f'Aluno ** Aprovado! ** Sua média é: {media:.2f}')    
else:
    print (f'Aluno ** Reprovado **, sua média é: {media:.2f}')















































