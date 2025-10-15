""" 
LEMBRE-SE:
=========
As f-strings servem para que você consiga 
colocar uma variável dentro de um texto, e isso é 
feito utilizando a letra “f” antes do texto e colocando 
a sua variável dentro de {} chaves.

Isso é muito útil para que você não tenha que ficar 
concatenando o seu texto com as variáveis e tenha que 
fatiar seu texto várias vezes por conta disso. 

"""
'''
ATENÇÃO:
=======
para trabalhar com datas use: from datetime import datetime

Explicação: from [biblioteca] import [ferramenta específica]

'''

# Bibliotecas do Python:

# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

# Biblioteca: DATETIME https://docs.python.org/3/search.html?q=datetime

# 1) Crie um código Python que leia dois números e
# mostre a soma entre eles
# \n = new line ( enter dentro do terminal )
n1 = int(input('Primeiro número: \n'))
n2 = int(input('Segundo número: \n'))

# a soma dos valores é:
print(f'A soma é: {n1 + n2}')




# int = obriga a entrada de número
# input() = função para memorizar dados digitados por padrão é do tipo texto
# \n = caracter para quebrar a linha (newline)
# com print mostre a soma entre eles

'''  
    Escreva seu código abaixo

    ***** ATENÇÃO: ao terminar de escrever o 
                   código vamos executar com: Debug
'''


# 2) Crie um script Python que leia: o dia, o mês e o ano de nascimento
# de uma pessoa e  mostre uma mensagem com a data formatada corretamente
'''
    O símbolo de %(porcentagem) funciona como marcador de substituição. 
    Ele indica que ali será inserido um valor específico da data,
    é usado para formatação de datas (e também de strings em geral).

    Código	Significado	            Exemplo
    %d      Dia do mês (2 dígitos)	01–31
    %m	    Mês (2 dígitos)	        01–12
    %y	    Ano (2 dígitos)	        24
    %Y	    Ano (4 dígitos)	        2024
    %H	    Hora (00–23)	        13
    %M	    Minutos	                45
    %S	    Segundos	            09

'''


# Escreva seu código abaixo

# 1o passo - importar/chamar o módulo para trabalhar com datas
import datetime

# 1972
ano = int(input('Ano de nascimento: '))

# 11
mes = int(input('Mês de nascimento: '))

# 05
dia = int(input('Dia de nascimento: '))

# 2o passo - converter (ano, mes, dia) no formato data
# obs.: faça a conversão no padrão Americano, caso contrário dará erro

# 1972-11-05
datanasc = datetime.datetime(ano, mes, dia)


# 2025-08-18
# 3o passo - exibir(print()) os dados
# exibir no padrão brasileiro (dd/mm/yyyy)
# 18-08-2025
# .strftime = converte a data data para texto 
# 05-11-1972
print(datanasc.strftime('%d/%m/%Y'))

