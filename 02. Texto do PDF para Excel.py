#lê dados de pdf
import pymupdf

import pandas as pd

import os

#criar uma lista vazia para guardar linhas do texto extraido do PDF
listas_texto = []

#item 1 - caminho do arquivo PDF
origem_pdf = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_01\bases\Salário Mínimo 2019.pdf'

#item 2 - camo-inho do arquivo excel que será criado com o texto do PDF
destino_excel = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_01\bases\Salário Mínimo 2019.xlsx'


#item 3 - abre o arquivo PDF no modo leitura binária (rb = read binary)
with pymupdf.open(origem_pdf) as pdf:

    #percorre todas as páginas do PDF, uma por uma
    for pagina in pdf:

        #extrai todo o texto da página
        texto = pagina.get_text('text')

        #se a página tiver texto (pode haver páginas em branco)
        if texto:

            #divide o texto em várias linhas(\n - quebrar linha)
            linhas = texto.split('\n')

            #adiciona todas as linhas dessa página na lista principal
            listas_texto.extend(linhas)

#sai do with

#item 4 - criar uma tabela (DataFrame) com uma única coluna chamada [Texto]
df = pd.DataFrame(listas_texto,columns = ['Texto'])

#item 5 - salvar a tabela em um arquivo excel, sem incluir o indice(index=false)
df.to_excel(destino_excel, index = False)

#item 6 - abrir o arquivo automaticamente após cria-lo
os.startfile(destino_excel)

























































































