'''
    LISTAS: 
        Adição 
        Remoção 
        Alteração de valores
        Ordenação

        
        * APPENDD >>> Atribui a lista, um elemento por vez. 
        * INSERT >>> Atribui vários elementos, integrando à lista original.
        * POP >>> Remove um valor da lista por índice.
        * REMOVE >>> Remove um valor da lista por valor.
        * SORT >>> Ordena os dados de uma lista.
        

'''

# Gerencimanto de estoque com listas
# escreva seu código abaixo
produtos = ['monitor', 
            'notebook',
            'teclado',
            'mouse']

print('Estoque inicial:')
print(produtos)

# adicionar novos podutos
produtos.append('impressora') # adiciona no final da lista
print(f'Adicionado a impressora: \n {produtos}')

# adiciona na 2a posição
produtos.insert(2, 'headset') #adiciona na posição informada(2)
print(f'Adicionando o headset na 2o posição: \n{produtos}')

# remover produtos
produtos.remove('mouse') #remove pelo nome
print(f'Removendo o mouse: \n{produtos}')

# remover pelo índice(posição) 1
removido = produtos.pop(1) #remove pelo indice(posição na lista)
print(f'Removendo o item 1 no indice (2o posição): \n{produtos}')

# alteração de produtos
# altera o primeiro item
produtos[0] = 'monitor led'
print(f'Alterando o primeiro item: \n{produtos[0]}')

# altera o último item
produtos[-1] = 'impressora a laser'
print(f'Alterando o último item: \n{produtos[-1]}')

# ordenação dos produtos
# ordenar em ordem alfabética [A-Z]
produtos.sort()
print(f'Alterar por ordem alfabética AZ: \n {produtos}')

# ordenação reversa [Z-A]
produtos.sort(reverse=True)
print(f'Altera por ordem alfabética ZA: \n{produtos}')















































































