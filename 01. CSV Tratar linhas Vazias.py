import pandas as pd

# =========================
# 1. Caminho do CSV
# =========================
caminho_csv = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_03\Aluno\CSV Tratar\01.Vendas Carros.csv'

# =========================
# 2. Lê o CSV
# =========================
# sep=';' -> seu CSV usa ponto e vírgula
# encoding='latin1' -> lê acentos corretamente
# dtype=str -> tudo como texto
df = pd.read_csv(caminho_csv, sep = ';', encoding='latin-1',dtype = str)

# =========================
# 3. Remove linhas vazias ou só com espaços
# =========================
# Lista para armazenar índices das linhas válidas
linhas_validas = []

# =========================
# 4. Salva de volta no CSV
# =========================
contador_vazias = 0

#percorre cada linha dentro do aruqivo
for idx, linha in df.iterrows():

    #remover os espaços de cada célula da linha
    linha_limpa = linha.fillna('').astype(str).str.strip()

    #se pelo menos uma célula houver valor, mantém a linha 
    if not linha_limpa.eq('').all():
        linhas_validas.append(idx)
    else:
        #linha totalmento vazia ou só com espaços
        contador_vazias += 1

#cria um DataFrame apenas com as linhas válidas
df = df.loc[linhas_validas]

#salvar os dados do DF de volta no CSV
df.to_csv(caminho_csv, sep = ';', index=False, encoding = 'latin-1')

# =========================
# 5. Mensagem final
# =========================
print (f'Fim do processamento.')
