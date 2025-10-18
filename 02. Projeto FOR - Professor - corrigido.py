""" 

Calcular de Salários Semanais empresa: XYZ Ltda
-----------------------------------------------

Crie um script que registre o salário diário 
de um funcionário por 5 dias úteis 
e calcule o salário total ao final da semana.

Pede-se:
========
Solicite para o usuário o valor do salário diário 
em cada dia útil, ou seja, de segunda a sexta-feira.
Use o for para somar os salários de todos os dias.
Mostre o total acumulado ao final.

Entrada:
=======

Digite o salário da segunda-feira: 
Digite o salário da terça-feira: 
Digite o salário da quarta-feira: 
Digite o salário da quinta-feira: 
Digite o salário da sexta-feira: 

Saída:
=====

Salário total da semana: 0.000.00

"""

# Lista/Arrays com dias úteis
dias_uteis = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
# Escreva seu código aqui

# 1o passo - Entrada
total_salario = 0

# 2o passo - For e cálculos
for diasemana in dias_uteis:
    salario_dia = float(input(f'Digite o salário do dia {diasemana}, valor R$ :'))
    total_salario += salario_dia

    
# 3o passo - saída
# Exibir o total acumulado do dia da semana
print(f'\nSalário total da semana: R$ {total_salario:.2f}')






