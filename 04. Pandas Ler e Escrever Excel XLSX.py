# 1o passo - chamar a biblioteca pandas
import pandas as pd

# lib serve para trabalhar com Windows/Linux
import os

# 2o passo - Local do arquivo Excel
local_arquivo = r'C:\Users\noturno\Desktop\Rafaélla Sena\Python I - Clarify\Aluno\CAPÍTULO 8 - LER E ESCREVER ARQUIVOS\Arquivo 1.xlsx'


# 3o passo - usar arquivo para pegar o número da aba
excel = pd.ExcelFile(local_arquivo)


# 4o passo - número da aba
numero_da_aba_arquivo = 0




# 5o passo - ao capturar o número da aba, ou seja, 
# sheet_name podemos identificar o nome dela
# a posição da aba dentro da planilha não pode ser alterada
# caso contrário o programa dá erro!
# Planilha 1
nome_aba = excel.sheet_names[numero_da_aba_arquivo]

print(f'Primeira aba: {nome_aba}')

if nome_aba != 'Planilha 1':
    print('A aba [Planilha 1] precisa ser a primeira')
    print('O programa será encerrado!')
    exit()
else:
    print('A Aba esta na posição correta.... processando....')


# 6o passo - ler a planilha pelo índice da aba (número)
df = pd.read_excel(local_arquivo, sheet_name = numero_da_aba_arquivo)


# 7o passo - adicionar umva nova coluna [Aumento 30%]
# se a coluna [Valor] não existe dentro do DataFrame(tabela)
if 'Valor' not in df.columns:
    print('Coluna[Valor] não existe!')
    exit()
else:
    ''' Se a coluna [Valor Aumento] não existe dentro do DataFrame(tabela), ou seja, dentro do arquivo, então crie a coluna e faça o cálculo'''
    if'Valor Aumento' not in df.columns:
        df['Valor Aumento'] = df['Valor'] + 1.30
        print('Coluna [Valor Aumento] criada com sucesso no DF')
    else:
        print('Coluna [Valor Aumento] já esxiste no arquivo, sem alterações!')
        os.startfile(local_arquivo)
        exit()

# 8o passo - escrever os da memória do DataFrame, no próprio Excel
# sheet_name=nome_aba, ou seja, "Planilha 1" que está dentro do arquivo
# obrigatoriamente precisa ser texto(string)
df.to_excel(local_arquivo, index=False, sheet_name=nome_aba,float_format='%.2f')


# 9o passo - abrir o arquivo onde ele está 
os.startfile(local_arquivo)






























