'''
Libs ( PANDAS  e OPENPYXL)
==========================

A biblioteca pandas é como uma super planilha dentro do Python. Ela permite:
----------------------------------------------------------------------------
1 - Ler arquivos Excel (.xlsx) e transformar em tabelas (DataFrames)
2 - Filtrar, ordenar, agrupar, somar, editar... tudo que você faria no Excel, mas com muito mais poder
3 - Salvar os dados de volta em um arquivo Excel

A openpyxl — Para interagir com o Excel em nível mais baixo
-----------------------------------------------------------
A biblioteca openpyxl é usada por trás dos panos para abrir, editar e 
salvar arquivos .xlsx. Ela entende a estrutura interna do Excel, como:
1 - Fórmulas
2 - Estilos (cores, fontes, bordas)
3 - Várias abas (sheets)
4 - Células mescladas, validações, etc.

Ela é usada como motor (engine) para o ExcelWriter do pandas. Sem ela, 
o pandas não conseguiria editar arquivos .xlsx com múltiplas abas corretamente.


Por que usar as duas juntas? ( cada uma tem um papel diferente )
----------------------------------------------------------------------------
| Função                        | pandas 🐼                 | openpyxl 📘 | 
----------------------------------------------------------------------------
| Manipular dados (tabelas)     | ✅ Sim                    | ❌ Não      | 
| Ler/escrever arquivos Excel   | ✅ Sim                    | ✅ Sim      | 
| Editar abas específicas       | ✅ Com ajuda do openpyxl  | ✅ Sim      | 
| Aplicar estilos/formatação    | ❌ Limitado               | ✅ Sim      | 
----------------------------------------------------------------------------

'''
# Passo 1: Importa bibliotecas necessárias
import pandas as pd
from openpyxl import load_workbook

# Passo 2: Define o caminho do arquivo Excel
arquivo_excel = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_06\Bases\Arquivo 1.xlsx'

# Passo 3: Lê as duas planilhas do arquivo
# planilha Destino (preencher colunas)
colab_df = pd.read_excel(arquivo_excel, sheet_name='Colaboradores')
base_df = pd.read_excel(arquivo_excel, sheet_name='Base Completa Colaboradores')

# Passo 4: Normaliza nomes de colunas e valores
# Remove espaços dos nomes das colunas
colab_df.columns = colab_df.columns.str.strip()
base_df.columns = base_df.columns.str.strip()

# Garante que a matrícula seja string e sem espaços
colab_df['Matricula'] = colab_df['Matricula'].astype(str).str.strip()
base_df['Matricula'] = base_df['Matricula'].astype(str).str.strip()

# Passo 5: Define as colunas que serão copiadas da base
colunas_dados = ['Departamento', 'Tipo', 'Empresa Aérea', 'Valor', 'Categoria', 'Forma Pgto']

# Passo 6
# Para cada nome de coluna que queremos garantir na planilha "Colaboradores"
for coluna in colunas_dados:
    if coluna not in colab_df.columns:
        colab_df[coluna] = None #vazio
    # Garante que o tipo de dado da coluna seja "object"
    # No pandas, "object" geralmente significa texto (string)
    # Isso é importante para evitar erros ao preencher com 
    # dados mistos (texto, número, etc.)
    colab_df[coluna] = colab_df[coluna].astype('object')    

# Passo 7: Cria dicionário indexado por matrícula com os dados da base
base_dict = base_df.set_index('Matricula')[colunas_dados].to_dict('index')

# Passo 8: Atualiza os dados da planilha "Colaboradores" com base na matrícula
status_lista = []

# Percorre cada linha da planilha "Colaboradores"
# A função .iterrows() permite acessar linha por linha do DataFrame
# "i" é o número da linha (índice) e "row" é o conteúdo da linha 
# (como se fosse uma mini planilha)
for i, row in colab_df.iterrows():    

    # Pega o valor da matrícula da linha atual
    # Isso será usado para procurar os dados correspondentes 
    # no dicionário "base_dict"
    matricula = row ['Matricula']

    # Verifica se essa matrícula existe no dicionário "base_dict"
    # Se existir, significa que temos dados adicionais para esse colaborador
    if matricula in base_dict:

        # Para cada coluna que queremos preencher (como Departamento, Tipo, etc.)
        for coluna in colunas_dados:

            # Atualiza a célula da linha atual com o valor correspondente do dicionário
            # Exemplo: colab_df.at[3, "Departamento"] = "TI"
            colab_df.at[i,coluna] = base_dict[matricula][coluna]
            
        # Adiciona "Encontrado" à lista de status, indicando que os dados foram preenchidos
        status_lista.append('Encontrado')

    else:
        # Se a matrícula não estiver no dicionário, marca como "Não encontrado"
        # Isso ajuda a identificar quais colaboradores não têm dados na base
        status_lista.append('Não encontrado')

# Passo 9: Adiciona coluna de status à planilha "Colaboradores"
colab_df['Status'] = status_lista

# Passo 10: Salva a aba "Colaboradores" sem apagar as outras abas do Excel
# Abre o arquivo Excel existente para edição usando o ExcelWriter
# O parâmetro "engine='openpyxl'" permite trabalhar com arquivos .xlsx que têm várias abas
# O parâmetro "mode='a'"(append) significa que vamos "adicionar" conteúdo ao arquivo existente (sem apagar tudo)
# O parâmetro "if_sheet_exists='replace'" diz que, se a aba "Colaboradores" já existir, ela será substituída pelos dados novos
with pd.ExcelWriter(arquivo_excel, engine = 'openpyxl', mode = 'a', if_sheet_exists='replace') as writer:
  
    # Escreve os dados atualizados do DataFrame "colab_df" na aba chamada "Colaboradores"
    # O parâmetro "index=False" evita que o número da linha (índice) seja 
    # salvo como uma coluna extra no Excel
    colab_df.to_excel(writer, sheet_name='Colaboradores', index=False)

# Passo 11: Exibe mensagem de sucesso
print ('Aba [Colaboradores] atualizada com sucesso')








