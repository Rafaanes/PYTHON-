# Biblioteca: DATETIME

# https://docs.python.org/3/search.html?q=datetime

# Basic date and time types
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

'''
    Tabela de códigos de formatação de datas e horas (strftime)

    Código	Significado	                        Exemplo
    %d	    Dia do mês (2 dígitos)	            02
    %m	    Mês (2 dígitos)	                    05
    %Y	    Ano com 4 dígitos	                2025
    %y	    Ano com 2 dígitos	                25
    %H	    Hora (formato 24h)	                14
    %I	    Hora (formato 12h)	                02
    %M	    Minutos	                            09
    %S	    Segundos	                        45
    %f	    Microssegundos	                    123456
    %A	    Nome completo do dia da semana	    sexta-feira
    %a	    Nome abreviado do dia da semana	    sex
    %w	    Número do dia da semana (0–6)	    5 (sexta-feira)
    %B	    Nome completo do mês	            maio¹
    %b	    Nome abreviado do mês	            mai¹
    %p	    AM/PM (em inglês)	                AM ou PM
    %j	    Dia do ano (001–366)	            123
    %U	    Semana do ano (domingo = início)	17
    %W	    Semana do ano (segunda = início)	18
    %c	    Data e hora local completas	        Sex 02 Mai 2025 14:15:00
'''

'''
    '%w' = retorna o dia da semana
    
    0 = domingo
    1 = segunda-feira
    2 = terça-feira
    3 = quarta-feira
    4 = quinta-feira
    5 = sexta-feira
    6 = sábado 
'''

# Vamos consolidar o aprendizado com IFs

# ATENÇÃO: VAMOS USAR, *** DEBUGGIN PYTHON FILE ***,
# para finalizar o processo 

# ==================================

'escreva seu código aqui'
from datetime import datetime

numero_dia_da_semana = datetime.now().date().strftime('%w')

if numero_dia_da_semana == '0':
    print('domingo')
elif numero_dia_da_semana == '1':
    print('segunda-feira')
elif numero_dia_da_semana == '2':
    print('terça-feira')
elif numero_dia_da_semana == '3':
    print('quarta-feira')
elif numero_dia_da_semana == '4':
    print('quinta-feira')
elif numero_dia_da_semana == '5':
    print('sexta-feira')    
else:
    print('Sabádo')


























































































