'''
O que esse programa faz
=======================
1) Cria um pequeno conjunto de dados (meses e vendas).

2) Transforma esses dados em uma tabela do pandas (DataFrame).

3) Gera um gráfico de linha interativo com Plotly.

4) Cria um site simples com o Dash contendo o título e o gráfico.

5) Quando você roda o código, ele abre um servidor local (geralmente em http://127.0.0.1:8050),
e o gráfico aparece no navegador.

Como rodar:
Salve o código em um arquivo chamado app.py 
e execute com:

    python app.py

'''
# pip install dash
# pip install plotly
# pip install pandas

# Dica: Se quiser instalar tudo junto, use:
# pip install dash plotly pandas


# Pandas: biblioteca para manipulação e análise de dados (tabelas, planilhas, etc.)
import pandas as pd

# Dash: biblioteca para criar aplicativos web interativos com Python
import dash

# html e dcc (Dash Core Components): módulos usados para criar os elementos visuais da página
# html -> usado para colocar textos, títulos, divisões, etc.
# dcc -> usado para criar gráficos e componentes interativos (menus, sliders, etc.)
from dash import html, dcc

# Plotly Express: biblioteca que cria gráficos bonitos e interativos de forma simples
import plotly.express as px

# Dash.dependencies: usada para conectar componentes interativos
# (exemplo: se o usuário mudar um menu, atualizar o gráfico automaticamente)
from dash.dependencies import Input, Output

# -----------------------------------------------------------
# ETAPA 1 - CRIAR OS DADOS FICTÍCIOS
# -----------------------------------------------------------

# Lista com os nomes dos meses (será o eixo X do gráfico)
meses = ['janeiro','fevereiro','março','abril','maio','junho']

# Lista com os valores de vendas correspondentes a cada mês (será o eixo Y do gráfico)
vendas = [100, 120, 130, 90, 150, 170]

# -----------------------------------------------------------
# ETAPA 2 - CRIAR UM DATAFRAME (TABELA)
# -----------------------------------------------------------

# Criamos um DataFrame (tabela) com 2 colunas:
# 'Mês' -> contendo os nomes dos meses
# 'Vendas' -> contendo os números de vendas
df = pd.DataFrame({'Mês' : meses, 'Vendas' : vendas }) #nome da primeira coluna e segunda coluna

# O resultado do DataFrame "df" fica assim:
#      Mês       Vendas
# 0  janeiro      100
# 1  fevereiro    120
# 2  março        130
# 3  abril         90
# 4  maio         150
# 5  junho        170

# -----------------------------------------------------------
# ETAPA 3 - CRIAR O GRÁFICO
# -----------------------------------------------------------

# Criamos um gráfico de linha (line chart) com a biblioteca Plotly Express.
# Esse gráfico mostrará a evolução das vendas ao longo dos meses.
figura = px.line(
    df, #dados que serão usados (tabela)
    x='Mês', #eixo x 
    y= 'Vendas', # eixo y
    title= 'Vendas Mensais'
)

# -----------------------------------------------------------
# ETAPA 4 - INICIAR O APLICATIVO DASH
# -----------------------------------------------------------

# Criamos o objeto principal do app.  
# "__name__" (com dois underlines antes e depois) indica o nome do módulo Python atual.
# Isso é necessário para o Dash saber onde o app está sendo executado.
# Ela guarda o nome do arquivo Python atual.
# Imagine que:
# - dash → é uma empresa de construção de sites;
# - Dash() → é o engenheiro que começa um novo projeto;
# __name__ → é o endereço do terreno onde ele vai construir.
app = dash.Dash(__name__)

# -----------------------------------------------------------
# ETAPA 5 - DEFINIR O LAYOUT DO APP (APARÊNCIA DA PÁGINA)
# -----------------------------------------------------------

# O layout define o que será exibido na tela: títulos, gráficos, botões etc.
# "Div" é uma divisão (bloco) da página
# html.H1('Dashboard de Vendas') título principal, tamanho H1 (grande)
# dcc.Graph = Componente de gráfico interativo (Plotly)
# gráfico que criamos na etapa 3
app.layout = html.Div([
    html.H1('Dashboard de Vendas Mensais'),
    dcc.Graph(id='grafico-vendas', figure= figura)
])

# -----------------------------------------------------------
# ETAPA 6 - EXECUTAR O SERVIDOR WEB
# -----------------------------------------------------------
'''
O __main__ não vem do seu código, nem de nenhuma biblioteca.
Ele vem do próprio interpretador Python (ou seja, do “cérebro” do Python).
É o Python que cria automaticamente o valor '__main__' toda vez que você executa um arquivo

Essa parte garante que o app será executado quando o arquivo for aberto diretamente.
"if __name__ == '__main__':" é um padrão do Python para indicar “rode este código se o arquivo for o principal”.
app.run() inicia o servidor local (localhost)
debug=False evita mostrar mensagens de depuração no terminal

Programa principal Python
│
├── Variável especial: __name__
│     ├── "__main__" → se o arquivo está sendo executado diretamente
│     └── "nome_do_arquivo" → se está sendo importado
│
├── Condição:
│     if __name__ == '__main__':
│          ↓
│          Executa o que está dentro (ex: inicia o app Dash)
│
└── app.run(debug=False)
       ├── app.run() → liga o servidor web local
       └── debug=False → roda o servidor em modo normal (sem recarregar)

'''
if __name__ == '__main__':
    app.run(debug=False)


















































