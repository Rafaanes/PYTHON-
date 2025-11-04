# ============================================
# DASHBOARD DE VENDAS DE CARROS - GRÁFICOS DE COLUNAS
# ============================================

# =======================
# PASSO 1: Importação das bibliotecas
# =======================
import pandas as pd
#para criar dashboards interativos na web
from dash import Dash, dcc, html 
#para criar interação(filtros e gráficos)
from dash.dependencies import Input, Output
#para criar gráficos de forma simples
import plotly.express as px
#lib para tratar vslores no padrão brasileiro
import locale

# =======================
# PASSO 2: Configurar locale para moeda brasileira
# =======================
try:
    #linux/MAC
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, 'Portugues_Brazil.1252')

def converter_valor(valor):
    #isna = is not avaliable (é indisónível)
    if pd.isna(valor):
        return 0
    #se já for número, retorna diretamente
    if isinstance(valor,(int,float)):
        return float(valor)
    
    #remover espaços
    valor = str(valor).strip()

    #remove ponto de milhar e troca por virgula por ponto decimal = padrão americano
    valor = valor.replace('.','').replace(',','.')

    try:
        return float(valor)
    except:
        return 0 

# =======================
# PASSO 3: Ler dados do Excel
# =======================
caminho_arquivo = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_03\Aluno\Dashboard\01.Vendas Carros.xlsx'

df = pd.read_excel(caminho_arquivo, sheet_name='Planilha1')

# =======================
# PASSO 4: Limpeza e tratamento de dados
# =======================
#remove espaços extras e colocam nomes das colunas em maiusculas
df.columns = df.columns.str.strip().str.upper()

# remove linhas totalmente vazias 
df.dropna(how='all', inplace=True)

#converter colunas monetárias em float
colunas_valores = ['PRECO_VENDA','ACESSORIOS','TOTAL_VENDAS']

#traduçaõ: para cada coluna dentro da lista de colunas do nosso DF, faça a conversão dos valores com as função
for col in colunas_valores:
    df[col] = df[col].apply(converter_valor)

#converter coluna de datas para o formato datetime 
df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True, errors = 'coerce')

# =======================
# PASSO 5: Criar o aplicativo Dash
# =======================
app = Dash(__name__)
app.title = 'DashBoard de Vendas de Carros'

# =======================
# PASSO 6: Definir o layout do dashboard
# =======================
app.layout = html.Div([
    html.H1('Dashboard de Vendas de Carros', style = {'textAlign':'center'}),
    html.Hr(),

    #filtros
    html.Div([
        html.Label('Selecione Estado: '),
        dcc.Dropdown(
            options=[{'label': uf, 'value': uf} for uf in sorted(df['UF'].dropna().unique())],
            id = 'filtro_estado',
            multi=True,
            placeholder = 'Todos os Estados'),
        html.Label('Selecione Marca:'),
        dcc.Dropdown(
            options=[{'label': marca, 'value': marca} for marca in sorted(df['MARCA'].dropna().unique())],
            id = 'filtro_marca',
            multi=True,
            placeholder = 'Todas as Marcas')        
    ], style= {'width':'48%','display':'inline-block'}),
    html.Br(), html.Br(),

    #gráficos
    html.Div([dcc.Graph(id='grafico_vendas_marca'),
            dcc.Graph(id='grafico_vendas_vendedor')
            ])            
])



# =======================
# PASSO 7: Criar a função que atualiza os gráficos
# =======================
def atualizar_graficos(estados_selecionados, marcas_selecionadas):

    df_filtrado = df.copy() #cria cópia do DataFrame

    #aplica filtros de Estado e Marca
    if estados_selecionados:
        df_filtrado = df_filtrado[df_filtrado['UF'].isin(estados_selecionados)]

    if marcas_selecionadas:
        df_filtrado = df_filtrado[df_filtrado['MARCA'].isin(marcas_selecionadas)]

    # Gráfico 1: MARCA X TOTOAL VENDAS
    vendas_marca = df_filtrado.groupby('MARCA')['TOTAL_VENDAS'].sum().reset_index()
    fig_marca = px.bar(
        vendas_marca,
        x= 'MARCA',
        y= 'TOTAL_VENDAS',
        text='TOTAL_VENDAS',
        title='Total de Vendas por Marca',
        color = 'MARCA'
    )

    #configura o texto das barras para mostrar valores dormatados com virgula e duas casas decimais
    fig_marca.update_traces(texttemplate='%{y:,.2f}', textposition='outside')
    fig_marca.update_layout(yaxis_title='Vendas (R$)')

    #Gráfico 2 = VENDEDOR X TOTAL VENDAS
    vendas_vendedor = df_filtrado.groupby('VENDEDOR')['TOTAL_VENDAS'].sum().reset_index()
    fig_vendedor = px.bar(
        vendas_vendedor,
        x='VENDEDOR',
        y='TOTAL_VENDAS',
        text='TOTAL_VENDAS',
        title = 'Total de Vendas por Vendedor',
        color='VENDEDOR'
    )
    fig_vendedor.update_traces(texttemplate='%{y:,.2f}', textposition='outside')
    fig_vendedor.update_layout(yaxis_title='Vendas (R$)')

    #retorna os dois gráficos
    return fig_marca,fig_vendedor


# =======================
# PASSO 8: Registrar a função nos callbacks do Dash sem usar decorator
# =======================
# Aqui "conectamos" a função aos gráficos e filtros
app.callback(
    Output('grafico_vendas_marca', 'figure'),
    Output('grafico_vendas_vendedor', 'figure'),
    Input('filtro_estado', 'value'),
    Input('filtro_marca', 'value')
)(atualizar_graficos)

# =======================
# PASSO 9: Executar o servidor Dash
# =======================
if __name__ == '__main__':
    #dash em execução
    app.run(debug=True)




















