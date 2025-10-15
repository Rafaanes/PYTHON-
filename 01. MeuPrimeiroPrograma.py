# 1o passo - crie um código para exibir uma mensagem
# de boas vindas
print('Olá Mundo!')
print("Olá Mundo!")

# 2o passo - crie uma variável do tipo texto que permita
# a entrada de dados
# input() = é um método de entrada de dados
nome = input('Digite seu nome: ')

# 3o passo - forma Errada de exibir o contéudo da variável
print('Olá Mundo {nome} ! Prazer em conhecer.')

# 4o passo - modo correto para exibir o conteúdo da variável
'''
{} = chaves irá receber o conteúdo da variável de entrada(input())
.format = é o método para receber o conteúdo da variável

'''
print(f'Olá {nome} ! Prazer em conhecer.')

# 5o passo - valor float
'''
.2f = tudo que vier após o ponto considere 2 casas decimais
f = format
f = format será usado quando desejamos juntar/unir variáveis 
com textos
ou texto com números/valores

'''
print(f'Preço R$ {25.12345:.2f} float(valor monetário)')

# outra maneira de arredondar
print(f'Preço R$ {round(35.75692,2)} função round')

# valor inteiro
print(f'O valor inteiro é: {8.9:.0f}')

# valor formatado em porcentagem
print(f'O valor formatado em porcentagem é: {10.123456:.2f}%')
