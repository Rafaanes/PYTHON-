# -----------------------------------------------------------
# 1 IMPORTAÇÃO DE BIBLIOTECAS
# -----------------------------------------------------------

# dash: biblioteca para criar aplicativos web interativos com Python
import dash

# html e dcc: módulos do Dash para criar componentes visuais
# html -> textos, títulos, divisões (como uma página HTML)
# dcc (Dash Core Components) -> gráficos, menus dropdown, sliders, etc.
# Input e Output -> usados para “conectar” elementos interativos (callbacks)
from dash import html,dcc
from dash.dependencies import Input, Output

# plotly.express: biblioteca para criar gráficos bonitos de forma simples
import plotly.express as px

# pandas: biblioteca para trabalhar com dados em tabelas (DataFrames)
import pandas as pd

# -----------------------------------------------------------
# 2 CRIAR DADOS FICTÍCIOS
# -----------------------------------------------------------

# Lista de meses (eixo X do gráfico)
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Lista de vendas correspondentes a cada mês (eixo Y do gráfico)
vendas = [100, 120, 130, 90, 150, 170]

# -----------------------------------------------------------
# 3️ CRIAR UM DATAFRAME (TABELA)
# -----------------------------------------------------------

# DataFrame = tabela de dados organizada em colunas
# Aqui criamos 2 colunas: 'Mês' e 'Vendas'
# 'Mês' : mes = coluna com os meses
# 'Vendas' : vendas = coluna com os valores de vendas
df = pd.DataFrame ({'Mês' : mes, 'Vendas' : vendas})

# -----------------------------------------------------------
# 4️ INICIALIZAR O DASH
# -----------------------------------------------------------

# Cria o objeto principal do app Dash
# __name__ indica que este arquivo é o principal que está sendo executado
app = dash.Dash (__name__)

# -----------------------------------------------------------
# 5️ DEFINIR O LAYOUT (APARÊNCIA DO DASHBOARD)
# -----------------------------------------------------------

# app.layout = define toda a estrutura da página
# html.Div = “divisão” ou bloco na página
app.layout = html.Div ([
    #titulo principla da página
    html.H1('Dashboard de Vendas Interrativo'),
    #dropdown
    dcc.Dropdown(
        id='filtro-mes',
        options = [{'label': mes, 'value': mes} for mes in df ['Mês']],
        #criar opções automáticas de seleção de meses
        value=mes, #valor inicial do drop 
        multi=True, #perimite filtrar por mais de uma opção
        placeholder = 'Selecione os meses' #texto no box quando não ha seleção de filtro
    ),
    #componente para mostrar o gráfico
    #o gráfico será atualizado quando o usuario mudar o dropdown(filtrar)
    dcc.Graph(id='grafico-vendas')
])

# -----------------------------------------------------------
# 6️ CALLBACK = LIGA FILTRO AO GRÁFICO
# -----------------------------------------------------------

# Conecta o dropdown ao gráfico
# Sempre que o usuário selecionar ou alterar os meses no dropdown,
# esta função será executada para atualizar o gráfico
@app.callback(
    Output('grafico-vendas', 'figure'), #saida do grafico que será atualizado após filtrado(entrada)
    Input('filtro-mes', 'value') #entrada = meses selecionados no dropdown(filtro)
)

def atualizar_grafico(meses_selecionados):
    #função que atualiza o grafico com base nos meses selecionados

    #filtra a tabela original com os meses escolhidos
    df_filtrado = df[df['Mês'].isin(meses_selecionados)]

    #criar um gráfico de linha com os dados filtrados
    fig = px.line(
        df_filtrado,
        x='Mês',
        y='Vendas',
        title = 'Vendas por Mês (filtrado)'
    )
    return fig
# -----------------------------------------------------------
# 7️ EXECUTAR O APP
# -----------------------------------------------------------

# Esse comando inicia o servidor web local
# O navegador abrirá em http://127.0.0.1:8050
if __name__ == '__main__':
    app.run(debug=False, port=8051)






















