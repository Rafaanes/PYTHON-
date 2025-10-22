# escreva seu código aqui

# 1o passo - importar lib pandas
import pandas as pd


# lib para trabalhar com Windows
# os = object system (objeto do sistema)
import os



# Função - Conversão de Valor para formato Americano
def converter_valor (receber_valor):
    
    receber_valor = str(receber_valor)
    
    #remove separador de milhar
    receber_valor = receber_valor.replace('.','')
    
    #substituir vírgula decimal para ponto
    receber_valor = receber_valor.replace(',','.')
    
    #transformou o valor no formato Americano para permitir os cálculos na coluna
    return float(receber_valor)

# 2o passo - Local do CSV - Inicio do programa

# r = raw string (lê todo o texto como string bruta)
# seu principal objetivo evitar problemas aos ler as barras
local_arquivo = r'C:\Users\noturno\Desktop\Rafaélla Sena\Python I - Clarify\Aluno\CAPÍTULO 8 - LER E ESCREVER ARQUIVOS\Vendas Regionais CSV.csv'


# 3o passo - utilizar o Pandas para ler o CSV
df = pd.read_csv(local_arquivo, delimiter= ";")
print(df.head())


# 4o passo
# aplica a função a coluna 'Vendas'
# caso contrário não podemos realizar o cálculo
# é necessário usar .apply(converter_valor) que é função
# onde captura ada valor dentro do CSV que está no padrão
# Brasileiro e transforma no formato Americano
# para permitir os cálculos
df['Vendas'] = df['Vendas'].apply(converter_valor)




# 5o passo - verificar se não existe a coluna 'Vendas' dentro
# do próprio DataFrame antes de fazer qualquer operação com ela

# se a coluna 'Vendas' não está dentro do DataFrame então 
# vamos tratar
# tradução: se a coluna 'Venda' não existe dentro das colunas
# do DataFrame(tabela), então mostrar mensagem

if'Vendas' not in df.columns:
    print('Coluna [VENDAS] não existe no arquivo')
    exit()
else:
    if 'Total com imposto' not in df.columns:
        #se a coluna [Total com imposto] não esxiste no arquivo então, criamos no DataFrame(tabela) ela o resultado do cálculo
        df['Total com imposto'] = df['Vendas'] + (df['Vendas'] * 0.2)
        print('Coluna [Total com imposto] criada com sucesso!')
        
    else:
        print('Coluna [Total com imposto] já existe no arquivo')
        print('O programa será encerrado...')
        os.startfile(local_arquivo)
        exit()
        
# 6o passo - salva o DataFrame atualizado
# com a nova coluna se ela foi criada no CSV
# index=True (ou omitido) = salva o número da linha como coluna
# index=False = não salva o número da linha, apenas os dados reais
# sep=; indica o formato do separador do CSV
# %.2f indica o número de casas decimais na coluna
# enconding='utf-8-sig' codifica padrão unicode mais usado no mundo para
# ler todos os idiomas
# Vamos escrever tudo que está no DataFrame(tabela) dentro do Excel
df.to_csv(local_arquivo, sep=';', index=False, decimal=',', float_format='%.2f', encoding='utf-8-sig')



# 7o passo - imprimir uma mensagem 
print(f'Arquivo salvo no local: {local_arquivo}')
      

# 8o passo - faz o Windows abrir o arquivo no local onde foi salvo
os.startfile(local_arquivo)























































