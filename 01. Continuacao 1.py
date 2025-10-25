
'''
Cenário proposto:
================

1) Ler dados de duas planilhas(abas) diferentes dentro do mesmo arquivo Excel:

    De uma planilha vamos pegar as informações do cliente e da cidade.

    De outra planilha vamos pegar o plano que o cliente comprou e o valor mensal que ele paga.

2) Limpar os dados:

    Remover linhas que estejam incompletas (com informações faltando).

    Ajustar o valor mensal para ter só 2 casas decimais.

3) Juntar essas duas partes dos dados em uma tabela só:

    Para cada cliente, juntar os dados da cidade, 
    plano e valor mensal na mesma linha.

4) Adicionar novas colunas na tabela:

    Criar uma coluna "ID" que numera cada linha.

    Adicionar uma coluna "País" com o valor "Brasil" em todas as linhas.

    Calcular um desconto baseado no tipo de plano (exemplo: plano Pro tem 5% de desconto, Regular tem 10%, outros planos 15%) e coloca esse valor na coluna "Desconto".

5) Salvar essa nova tabela em um arquivo Excel novo.

6) Depois, o código lê esse novo arquivo, faz uma 
   última atualização (confere se as colunas "ID" e "País" estão lá 
   e atualiza os valores) e recalcula os descontos para garantir que tudo esteja certo.

7) Por fim, imprime essa tabela organizada e atualizada na tela para você ver.


RESUMO:
=======
Esse código lê dados de clientes e planos de um arquivo Excel, 
organiza e limpa esses dados, calcula descontos e
salva tudo num arquivo novo pronto para ser usado.


'''
# Importa a lib
import pandas as pd
import os

#1o função - que recebe o caminho do arquivo e realiza o tratamento dos dados
def tratamento(caminho):

    #aba planilha 4
    dados_p1 = pd.read_excel(
        caminho, #caminho do arquivo excel
        sheet_name=3, #ler a planilha de indice 3(aba)[começa a contagem do 0]
        #pular as 4 primeiras linhas (indice leia-se: 0,1,2,3...) desta maneira localiza o cabeçalho
        skiprows=4,
        #dados ausentes/células vazias
        na_values=['N/A','NaN'],
        #ler somente as colunas 'Cliente' e 'Cidade'
        usecols=['Cliente','Cidade']
    )
    #aba Planilha 2
    dados_p2 = pd.read_excel(
        caminho,
        sheet_name=1,
        skiprows=10,
        na_values= ['N/A','NaN'],
        usecols=['Plano Vendido','Valor Mensal'],
        dtype= {'Valor Mensal': float} #chaves para ler valor
    )

    #arredondar os valores da coluna [Valor Mensa] em duas casas decimais
    dados_p2['Valor Mensal'] = dados_p2['Valor Mensal'].round(2)

    #remove linhas como valores ausentes em ambos os DataFrames
    dados_p1= dados_p1.dropna() #drop(apagar na- not available/não disponivel)
    dados_p2= dados_p2.dropna()

    #juntar os dois DataFrames em 1 só, linha a linha pelo indice
    dados = pd.merge(dados_p1,dados_p2,
                     left_index=True, #mesclar usando o indice dos dados_p1(esquerda)
                     right_index=True #mesclar usando o indice dos dados_p2(direita)
                     )
    
    #comentario que vem a seguir pode ser feito fora da função, mas está aqui devido a estrutura dos dados
    #reset (limpar) o indice do DataFrame para começar do zero, descartando o indice anterior
    #drop=True(apagar o indice) inplace=True(no proprio DataFrame)
    dados.reset_index(drop=True,inplace=True)

    #ajustar o indice para começar em  1 ao inves de o(mais amigavel)
    #tradução: dados.index = dados,index +1
    dados.index += 1

    #guardar o indice atual (que vai servir como ID)
    id = dados.index

    #adicionar uma coluna [ID] numerada sequencialmente
    dados.insert(
        loc=0, #insete na posição 0 (primeira coluna)
        column='ID', #nome da coluna
        value=id #valores para essa coluna (indice)
    )

    #adicionar uma coluna chamada [País] como valor fixo [Brasil] para todas as linhas
    dados.insert(
        loc=3, #inserir na posição 3(quarta coluna, começa com zero)
        column='País', #coluna nova
        value='Brasil' #valor fixo para todas as linhas 
    )

    #### ATENÇÃO ####
    #vamos criar uma função: desconto_por_plano
    #cria uma nova coluna chamada [Desconto] na tabela = [dados]
    #para cada linha da tabela, aplica a função desconto_por_plano
    dados['Desconto'] = dados.apply(
        #usa a função anõnima(lambda) que recebe cada linha(row) e chama a função desconto_por_plano, passando os valores da linha
        lambda row: desconto_por_plano(
            row['Plano Vendido'],
            row['Valor Mensal']),
            # axis = 1 (calcular linha a linha em vez de coluna)
        axis=1
            
    )
    #retorna os dados tratados e caminho do arquivo 
    return dados, caminho 

#2a função - localiza no DataFrame o tipo de plano e aplica o desconto
def desconto_por_plano(plano,valor_mensal):
    #função que calcula o valor com desconto, conforme o tipo de plano
    if plano == 'Pro':
        return valor_mensal * (1 - 0.05) #desconto de 5%
    elif plano == 'Regular':
        return valor_mensal * (1 - 0.10) #desconto de 10%
    else:
        return valor_mensal * (1 - 0.15) # desconto de 15%
    
#3a função
#index=False (informa ao pandas, que você não quer salvar o indice do DataFrame no Excel como primeira coluna)7
def salvar_novoarquivo(dados, nome_planilha,caminho_novo):
    try:
        dados.to_excel(caminho_novo, sheet_name=nome_planilha, index=False)
        print(f'Arquivo salvo no local: {caminho_novo}')
        os.startfile(caminho_novo)
    except:
        print('ATENÇÃO: o arquivo está aberto... feche e tente novamente')
###########################3 INICIO DO PROGRAMA ########################################
#1o passo - identificações dos arquivos
caminho_origem = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_01\bases\01_base_exe.xlsx'
caminho_novo_arquivo = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_01\bases\Resultado_base_exe.xlsx'

#nome da aba para o novo arquivo
nome_planilha = 'Relatório de vendas'

#2o passo - nesta estapa inicia o proceso de análise, onde vamos criar as funções: Salvar_novoarquivo e tratamento para executar o tratamento dos dados e salvar em novo arquivo.xlsx
salvar_novoarquivo(
    #pegar apenas o DataFrame da tupla retornada
    tratamento(caminho_origem)[0],
    nome_planilha,
    caminho_novo_arquivo
)

#3o passo
caminho = caminho_novo_arquivo

#lê o arquivo Excel tratado
df = pd.read_excel(caminho)

#reset do indice para começar do zero
df.reset_index(drop=True, inplace=True)

#ajustar o indice
df.index += 1

#criar varialvel id baseada no indice
id = df.index

#se a coluna [ID] existir nós vamos atualizar, senão encerre
if 'ID' in df.columns:
    df['ID'] = id
else:
    df.insert(loc=0, column = 'ID', value = 0)

#se a coluna [País] existir, atualiza, senão encerre

if 'País' in df.columns:
    df ['País'] = 'Brasil'
else:
    df.insert(loc=3, column='País', value='Brasil')
print(df)













































