'''
    For >>> Utilizada quando se sabe a quantidade de repetições,
    de forma que é obrigatório determinar o final da execução do laço.

    Sintaxe:
    for item in iteravel:
        bloco que será executado

    * Range -> limite

'''

# sintaxe

# for = para
# contador = localiza quantas vezes foi executado
# in = dentro
# range = limite

# Escreva seu código aqui
# contador = é uma variável definada
#            pelo programador e
#            sempre inicia com zero
# in = dentro
# range = limite do For(qtde de execuções)
# range(3) = irá percorrer o FOR inicío em 0 com término em 2,
#            tradução: 0, 1, 2


'''
    ENUNCIADO:
    ==========

    Peça o nome e preço de 3 produtos e mostre os dados no final.

    PARA CADA PRODUTO ATÉ O LIMITE

    Para numero_produto dentro limite(3):

        # Pede o nome do produto

        # Pede o preço e converte para float

        # Mostra o produto cadastrado com o preço formatado


'''

'Escreva seu código aqui'

for numero_produto in range(3):
    nome = input(f'Informe o nome do produto número {numero_produto}: ')
    preco = float(input(f' Produto número {numero_produto}. Informe o preço do produto: '))
    

    print(f'Produto número{numero_produto}\n Nome produto: {nome}\n Preço: {preco: .2f}')
    
#estou fora do FOR
print ('Fim do processamento')
    











































