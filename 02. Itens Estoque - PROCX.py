# Passo 1: Importa bibliotecas necessárias
import pandas as pd
from openpyxl import load_workbook

# Passo 2: Define o caminho do arquivo Excel
arquivo_excel = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_06\Bases\Arquivo 2.xlsx'

# Passo 3: Lê as duas planilhas do arquivo
classe_b_df = pd.read_excel(arquivo_excel, sheet_name='Estoque - Classe B')
itens_df = pd.read_excel(arquivo_excel, sheet_name='Itens no Estoque', skiprows=3, usecols = 'D:I')

# Passo 4: Normaliza nomes de colunas e valores
classe_b_df.columns = classe_b_df.columns.str.strip().str.upper()
itens_df.columns = itens_df.columns.str.strip().str.upper()

# Passo 5: Define as colunas que serão copiadas da base de itens
classe_b_df['MATERIAL'] = classe_b_df['MATERIAL'].astype(str).str.strip()
itens_df['MATERIAL'] = itens_df['MATERIAL'].astype(str).str.strip()

# Passo 6: Garante que todas as colunas existam na planilha "Estoque - Classe B"
colunas_dados = ['DESCRIÇÃO', 'TIPO ITEM', 'KANBAN', 'CLASSE', 'CONSUMO MÊS']

# Passo 7: Cria dicionário indexado por MATERIAL com os dados da base de itens
for coluna in colunas_dados:
    if coluna not in classe_b_df.columns:
        classe_b_df[coluna] = None
    classe_b_df[coluna] = classe_b_df[coluna].astype("object")

itens_dict = itens_df.set_index('MATERIAL')[colunas_dados].to_dict('index')

# Passo 8: Atualiza os dados da planilha "Estoque - Classe B" com base no MATERIAL
status_lista = []

for i, row in classe_b_df.iterrows():
    material = row['MATERIAL'] #chave de pesquisa PROCX
    if material in itens_dict:
        for coluna in colunas_dados:
            classe_b_df.at[i,coluna] = itens_dict[material][coluna]
        status_lista.append('Encontrado')
    else:
        status_lista.append('Não encontrado')

# Passo 9: Adiciona coluna de status à planilha "Estoque - Classe B"
classe_b_df['STATUS'] = status_lista

# Passo 10: Salva a aba "Estoque - Classe B" sem apagar as outras abas do Excel
with pd.ExcelWriter(arquivo_excel, engine = 'openpyxl', mode = 'a', if_sheet_exists='replace') as writer:
    classe_b_df.to_excel(writer, sheet_name='Estoque - Classe B', index=False)

# Passo 11: Exibe mensagem de sucesso
print('Fim do processamento')













