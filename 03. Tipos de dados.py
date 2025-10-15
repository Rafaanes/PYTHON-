"""
1) TIPOS DE DADOS
=================
Inteiros(int): números inteiros sem parte decimal (ex: 1, 2, 3).

Pontos Flutuantes(float): números com casas decimais (ex: 1.5, 3.14).

Textos (Strings): cadeias de caracteres (ex: 'Olá, mundo!', 'a', 'b', '!')

Booleanos(Verdadeiro / Falso): (ex: True, False). 
 
2) OPERADORES
=============
Aritméticos: +, -, *, / (adição, subtração, multiplicação, divisão).

Comparação: ==, !=, >, <, >=, <= (igual a, diferente de, maior que, 
menor que, maior ou igual a, menor ou igual a)

Lógicos: and, or, not (e, ou, não). 

3) STRINGS (formatações)
========================
.title =  converte a primeira letra de cada palavra em maiúscula 
.lower = converter todos os caracteres de uma string para letras minúsculas
.upper = converter todos os caracteres de uma string para letras maiúsculas


"""

# Bibliotecas do Python:
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

# ----------------------------------------------------------------
# Cadastro de usuário.

# Seu sistema deve solicitar as seguintes informações:
# ----------------------------------------------------
#  nome
#  nome de usuário
#  email
#  altura (1.85) float
#  idade int
#  senha

# Em seguida, faça imprimir/exibir os dados do usuário, lembre-se de garantir
# que os dados sejam recebidos nos seus respectivos tipos e apresentados
# com as formatações corretas para cada caso.

# ----------------------------------------------------------------

'''

    GETPASS 
    =======

    serve para ler senhas ou entradas do usuário sem exibir
    o que está sendo digitado na tela, ideal para situações 
    que exigem segurança.

''' 
'Escreva seu código abaixo'

import getpass # oculta a digitação da senha no terminal

# 1o passo - Entradas - variáveis
# Marcelo Sena
nome_completo = input('Nome Completo: ').title()
nome_usuario = input('Nome do usuário: ').lower() # minuscula

email = input('Seu melhor e-mail: ').lower() 
altura = input('Altura: (ex.: 1,88) ')
                   # 1,88
altura_modificada = altura.replace(',','.') # fica ex.: 1.88
idade = int(input('Idade: '))

# controle de acesso
usuario_correto = 'admin'
senha_correta = '123456'

# 2o passo - controle da senha
# a senha digita no terminal ficará oculta
senha = getpass.getpass('Agora digite a senha, ela ficará oculta ao digitar: ')

# 3o passo - exibir os conteúdos de cada variável
print(f'Nome completo: {nome_completo}')
print(f'Usuário: {nome_usuario}')
print(f'E-mail: {email}')
print(f'Altura: {altura_modificada}')
print(f'Idade: {idade}')

# 4o passo - verificação da senha
if nome_usuario == usuario_correto and senha == senha_correta:
    print('Login efetuado com sucesso!')
    
    
else: # senão


    print('Usuário ou senha incorreto!')

print('/nConfira os dados')

print(f'Nome do cliente: {nome_completo}')

print(f'Usuario: {nome_usuario}')

print(f'Altura: {altura}')

print(f'Usuário é maior de idade: {maior_idade}')

print(f'Nova senha: {nova_senha}')

print (f'Novo e-mail: {novo_email}')
          
