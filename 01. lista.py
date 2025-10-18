"""
Listas
Em outras linguagens é conhecida como Array, 
Vetor ou Matriz...

* Dinâmica >>> Não possui tamanho fixo e 
não preciso informar este tamanho.

* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. 
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* CLEAR >>> Limpa a lista.

A lista suporta vários valores de qualquer 
tipo(texto, número, boleano, flutuante e etc)

https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists


"""
#          0      1    2    3     4  5    6   7
lista = ['Joao', 30, 1.83, True, 30, 30, 30, 30]

# escreva seu código aqui
indice = 0

#usamos o laço for para percorrer cada item da lista

for item in lista:
        #exibir a posição (indice) e o conteúdo (item)
        print(f'Na posição: {indice}, temos: {item}')
        
        #após mostrar, aumentamos o valor do indice em 1, isso faz com que na próxima volta do looping(for) ele mostre a posição
        
        indice += 1 


















