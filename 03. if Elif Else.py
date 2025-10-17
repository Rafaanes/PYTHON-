
"""
IF,   = (significa SE)
ELIF, = (significa SENÃO SE)
ELSE  = (significa SENAO)

Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Resumo: tomar decisões lógicas com base em diferentes cenários

    Tabela - Operadores Relacionais

            ==	Igual a
            !=	Diferente
            >=	Maior ou igual
            >	Maior que
            <	Menor que
            <=	Maior ou igual
    
    Operadores Lógicos

            or	OU lógico
            and	E lógico
            not	Negação
"""


# Bibliotecas do Python:
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

# Biblioteca: DATETIME

# https://docs.python.org/3/search.html?q=datetime

# *****************************************

# Escreva seu código aqui

# 1o passo - Entradas - variáveis
#datetime = dd/mm/yyyy hh:mm:ss
from datetime import date


# .today() = 2025-08-18 (padrão Americano yyyy-MM-dd)
data_atual = date.today().strftime('%d/%m/%Y')
print(f'Data atual: {data_atual}')

# 2o passo - cálculos
nota1 = float (input('Nota 1: '))
nota2 = float (input('Nota 2: '))
nota3 = float (input('Nota 3: '))
nota4 = float (input('Nota 4: '))

media = sum([nota1, nota2, nota3, nota4]) / 4

# 3o passo - tomar decisões com IF´s
if media >= 7 and media <=10:
     print(f'Aprovado! Sua média é {media: .2f}')     
elif media >=5 and media <7:
        print(f'Recuperação! Sua média é {media: .2f}')        
elif media >=0 and media <5:
        resp = input('Seu boletim foi assinado: [S/N ]').lower()
        if resp == 's':
                print('OK! Aluno REPROVADO')  
        elif resp == 'n':
                print('Certo! Vou entrar em contato com os responsavéis!')
        else:
                print('Opção inválida!')                
else:
        print('Média inválida')




























































































































