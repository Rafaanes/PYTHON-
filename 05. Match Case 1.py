""" 
    Como Funciona o Match Case(encontrar caso)?
    
    Imagine que você tem uma variável e quer 
    executar diferentes ações dependendo do valor
    dessa variável. Antes do match case, 
    você provavelmente usaria uma série de 
    if, elif e else. 
    Agora, com o match case, você pode fazer 
    isso de forma mais estruturada. 
    Veja um exemplo básico: 

"""

""" 
O motivo do .weekday() começar em 0 para segunda-feira 
está relacionado a uma convenção internacional 
adotada em várias linguagens e padrões, que 
definem a semana começando na segunda-feira


    0	= Segunda-feira
    1	= Terça-feira
    2	= Quarta-feira
    3	= Quinta-feira
    4	= Sexta-feira
    5	= Sábado
    6	= Domingo 

"""
# Escreva seu código aqui

# chamar o módulo nativo do Python para
# trabalhar com data (datetime)
# from [modulo(contém tudo, dia, mês, ano e etc...)] import [classe]
# a [classe] = nós especificamos o que desejados dela

from datetime import datetime

# numero_dia_semana = recebe o número do dia da semana
numero_dia_semana = datetime.today().weekday()

# Match Case
# tradução: Encontrar Caso ?

match numero_dia_semana:  # | (entre)
    case 0:
        print('Segunda-feira')
    case 1:
        print('Terça-feira')
    case 2:
        print('Quarta-feira')
    case 3:
        print('Quinta-feira')
    case 4:
        print('Sexta-feira')
    case 5:
        print('Sabádo')
    case 6:
        print('Domingo')
    case _: # caso contrário/senão
            #o underline informa que caso as opções acimas na atendam, vamos exibir uma mensagem.
        print('Dia inválido')




















