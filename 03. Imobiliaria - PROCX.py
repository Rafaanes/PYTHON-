import pandas as pd
from openpyxl import load_workbook

# Caminho do arquivo Excel


def formatar_preco(valor):
    try:
        return f"{float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return valor  # Se não for número, mantém original

# Passo 1: Ler as planilhas
arquivo_excel = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_06\Bases\Arquivo 3.xlsx'

exercicio_df = pd.read_excel(arquivo_excel, sheet_name= 'Exercicio')
imob_df = pd.read_excel(arquivo_excel, sheet_name= 'Imobiliaria')

# Passo 2: Padronizar nomes de colunas
exercicio_df.columns = exercicio_df.columns.str.strip().str.upper()
imob_df.columns = imob_df.columns.str.strip().str.upper()

# Passo 3: Garantir que a coluna VENDA seja string
exercicio_df['VENDA'] = exercicio_df['VENDA'].astype(str).str.strip()
imob_df['VENDA'] = imob_df['VENDA'].astype(str).str.strip()

# Passo 4: Colunas que queremos preencher
colunas_dados = ['CORRETOR','TIPO','PREÇO']

# Passo 5: Garante que as colunas existam na aba "Exercicio"
for coluna in colunas_dados:
    if coluna not in exercicio_df.columns:
        exercicio_df[coluna] = None
    exercicio_df[coluna] = exercicio_df[coluna].astype('object')

# Passo 6: Criar dicionário com os dados da venda
imob_dict = imob_df.set_index('VENDA')[colunas_dados].to_dict('index')

# Passo 7: Preencher os dados
for i, row in exercicio_df.iterrows():
    #PROCX/PROCV
    venda = row['VENDA']
    if venda in imob_dict:
        for coluna in colunas_dados:
            exercicio_df.at[i, coluna] = imob_dict[venda][coluna]

# Passo 7.1: Formatando a coluna PREÇO no padrão brasileiro
exercicio_df['PREÇO'] = exercicio_df['PREÇO'].apply(formatar_preco)


# Passo 8: Salvar a aba atualizada
with pd.ExcelWriter(arquivo_excel, engine= 'openpyxl', mode = 'a', if_sheet_exists = 'replace') as writer:
    exercicio_df.to_excel(writer, sheet_name='Exercicio', index=False)

print('Aba [Exercicio] atualizada com sucesso!')




















