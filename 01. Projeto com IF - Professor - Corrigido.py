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

3) faça o cálculo do IMC = PESO / ALTURA ** 2 

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

from datetime import date

# 1o passo - declaração de variávies
nome = input('Nome:')
idade = int(input(f'{nome}, agora digite sua idade:'))
peso = float(input('Peso: '))
altura = float(input('Altura: '))

# 2o passo - calcular o IMC
imc = peso / altura ** 2

# 3o passo - analisar o IMC e exibir o resultado
if imc < 18.5:
    resultado = 'Abaixo do peso'
elif imc >= 18.5 and imc < 25:
    resultado = 'Peso Normal'
elif imc >= 25 and imc < 30:
    resultado = 'Excesso de peso'
elif imc >= 30 and imc < 35:
    resultado = 'Obsedidade Classe I'
elif imc >= 35 and imc < 40:
    resultado = 'Obsedidade Classe II'
elif imc >= 40 and imc < 60:
    resultado = 'Obesidade Classe III'
else:
    resultado = 'Valor anormal, considere recalcular!'

# 4o passo - exibir os resultados
print(f'Seu IMC é: {imc}\nResultado: {resultado}')

# 5o asso - exibir a data atual
data_atual = date.today().strftime('%d/%m/%Y')
print(f'Data atual: {data_atual}')