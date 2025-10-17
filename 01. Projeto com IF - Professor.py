"""
Agora você irá calcular o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:
______________________________________________
| Menor que 18.5      | Abaixo do peso       |
| Entre 18.5 - 24.9   | Peso Normal          |
| Entre 25.0 - 29.9   | Excesso de peso      |
| Entre 30.0 - 34.9   | Obesidade classe I   |
| Entre 35.0 - 39.9   | Obesidade classe II  |
| Maior ou igual 40.0 | Obesidade classe III |
----------------------------------------------

*********************************************
******** exercício com: IFs *****************
*********************************************

Pede-se:
=======

1) crie as variaveis: 
    nome, idade, peso, altura, imc

2) cada variável deverá receber o valor correto, ou seja,
   (texto, numérico, valor decimal e etc...)

3) faça o cálculo do IMC = PESO / ALTURA ** 2 (ao quadrado) 

4) utilize o if, elif, else para identificar o IMC:

    dentro de cada Se deverá ter uma variavel com nome: resultado,
    atribua a variavel o texto indicado abaixo

    Se o imc for menor do que 18.5
        resultado = 'Abaixo do peso'
    
    Se o imc for maior ou igual a 18.5 e o imc menor que 25
        resultado = 'Peso Normal'

    Se o imc for maior ou igual a 25 e o imc menor que 30
        resultado = 'Excesso de peso'

    Se o imc for maior ou igual a 30 e o imc menor que 35
        resultado = 'Obesidade classe I'

    Se o imc for maior ou igual a 35 e o imc menor que 40
        resultado = 'Obesidade classe II'

    Se o imc for maior ou igual a 40 e o imc menor que 60
        resultado = 'Obesidade classe III'

    Senão
        'Valor anormal, considere recalcular.'
   
5) exibir com o comando correto
   o resultado, ou seja, 'Seu IMC é: ????'

6) mostre a data atual no formato: dd/mm/yyyy

"""

# Escreva aqui seu código

# *********************************************
# ******** exercício com: IFs ** ***************
# *********************************************

# 1o passo - ENTRADAS

from datetime import date

data = date.today().strftime('%d/%m/%Y') 
print(f'Data: {data}')
nome = input('Nome: ')
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))


imc = peso / altura ** 2 

if imc < 18.5:
    print(f'Abaixo do peso!\nSeu IMC é {imc: .2f}')
elif imc >=18.5 and imc <25:
    print(f'Resultado normal! \nSeu IMC é {imc: .2f}')
elif imc >=25 and imc <30:
    print(f'Excesso de peso." \nSeu IMC é {imc: .2f}')
elif imc >=30 and imc <35:
    print(f'Obesidade classe I. \nSeu IMC é {imc: .2f}')
elif imc >=35 and imc <40:
    print(f'Obesidade classe II. \nSeu IMC é {imc: .2f}')
elif imc >=40 and imc <60:
    print(f'Obesidade classe III.\nSeu IMC é {imc: .2f}')
else:
    print('Valor anormal, considere recalcular')





































































