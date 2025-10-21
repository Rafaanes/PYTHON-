
"""     

PANDAS
======

Pandas é uma poderosa biblioteca de manipulação 
e análise de dados no Python, amplamente utilizada 
para trabalhar com dados estruturados, como tabelas 
ou planilhas. Ele fornece estruturas de dados 
rápidas e flexíveis para lidar com grandes volumes 
de dados de forma eficiente, e é particularmente 
eficaz no processamento de dados tabulares (como CSV, Excel, SQL, etc.).

Aqui estão algumas das principais funcionalidades do Pandas:

Estruturas de dados principais:

DataFrame: Uma estrutura de dados bidimensional que 
pode armazenar dados de diferentes tipos 
(inteiros, strings, floats, etc.), semelhante a uma 
tabela do Excel ou um banco de dados relacional.

"""
# 1o passo - importar a lib
import pandas as pd


# 2o passo - caminho do arquivo CSV
#r = raw string (faz a leitura no formato de texto bruto)
caminho_CSV = r'C:\Users\noturno\Desktop\Rafaélla Sena\Python I - Clarify\Aluno\CAPÍTULO 8 - LER E ESCREVER ARQUIVOS\Vendas Regionais CSV.csv'


# 3o passo - lêr o arquivo CSV, que está separado
# os campos com ponto e vírgula
# df = é uma variável que significa DataFrame para o Pandas
df = pd.read_csv(caminho_CSV, sep = ';')



# 4o passo - exibe as primeiras linhas no terminal
print(df.head())
print('--------------------------------------------------------------------------------')

# 5o passo - para ler n primeiras linhas
print(df.head(15))
print('---------------------------------------------------------------------------------')

# 6o passo - mostrar da linha 15 até a 20
print(df.iloc[15:21])
print('---------------------------------------------------------------------------------')

# 7o passo - mostrar as n últimas linhas
# lembre-se: o objetivo não é exibir todas as linhas para 
# não sobrecarregar o terminal, se necessário abra o arquivo
# e veja os dados
print(df.tail(20))













































