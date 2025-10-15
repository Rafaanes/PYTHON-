"""
    CADASTRO DE USUÁRIO.

    SEU SISTEMA DEVE SOLICITAR AS SEGUINTES INFORMAÇÕES:
        Nome completo, Nome de usuário, Email, Altura, Idade e Senha.

    Lembre-se de garantir que os dados sejam inseridos com 
    seus respectivos
    tipos de dados e que caso tenha sido inserido 
    espaços desnecessários, devem
    ser removidos.

    AGORA IMPRIMA AS SEGUINTES INFORMAÇÕES:
        - Nome Completo do cliente.
        - Nome de usuário em  letras maiúsculas.
        - Se o usuário é maior de idade.
        - Insira _2025 ao final da senha e a imprima.
        - Substiua o domínio do email por @gmail.com e
        apresente o novo email de acesso do usuário.
"""

# Bibliotecas do Python:
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

#Escreva seu código abaixo

# 1o passo - entradas - variáveis e seus tipos de dados
nome_completo = input('Nome do cliente: ').title()
nome_usuario = input('Nome do usuário: ').upper() # maiuscula
email = input('Seu melhor e-mail: ').lower() # minuscula

# agora vamos alterar o dominío do e-mail para "@gmail.com"
# o método .split('@') separa o e-mail em duas partes:
# antes e depois do "@"
# por exemplo, "joao@outlook.com" vira uma 
# lista: ['joao', 'outlook.com']
# pegamos só a parte antes do "@" para manter o nome do usuário
# [0] = para manter o nome do usuário 'joao'
# [1] = para pegar o domínio 'outlook.com'
#[0]joao
#[1]outlook.com
usuario_email = email.split('@')[0]

# dominio = posição da lista [1]
dominio = email.split('@')[1]
print(f'Seu domínio atual é: {dominio}')

# montamos o novo e-mail usando o nome do usuário e o domínio fixo
# "@gmail.com"
# joao@gmail.com
novo_email = usuario_email + '@gmail.com'
altura = input('Altura: (ex.: 1,88) ').replace(',','.')
idade = int(input('Digite sua idade: '))

# cria uma nova senha adicionando "_2025" ao final da senha original
senha = input('Cadastre a senha: ')

nova_senha = senha + '_2025'

# 2o passo - validar a senha
# len(nova_senha) = conta quantos digitos/caracteres tem a senha nova
# tradução: Se a qtde de caracteres(nova_senha) for maior do que 18, então
# exibir uma mensagem
# 123456_2025
if len(nova_senha) > 20:
    print(f'Senha maior de 18 caracteres!')
    print(f'O programa será encerrado, aqui!')
    exit() # encerra o programa aqui / stop / para tudo
else: # senão
    print('Senha dentro do limite de 18 caracteres! Programa processando...')

# 3o passo - validar a idade do cliente
# Tradução: se a idade for maior ou igual a 18, então
# a variável reebe = 'Sim', senão a varável recebe 'Não'
if idade >= 18:
    maior_idade = 'Sim'
else: 
    maior_idade = 'Não'


# 4o passo - Saídas (exibir/print)
print('\n Confira os dados')

# exibe o nome do cliente formatado


# exibir o nome do usuário em letras maiusculas


# exibe altura


# exibe se o usuário é maior de idade


# exibe a nova senha criada com o sufixo "_2025"


# exibe o novo e-mail, com domínio alterado para @gmail.com






