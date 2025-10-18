
# FATIAMENTO
# resumo: fatiamento de listas (ou list slicing, em inglês) 
# é uma técnica para acessar partes de uma lista usando
# a notação de colchetes com dois pontos
# lista[início:fim]

#  Análise de Pedidos Recentes com Fatiamento
#  Simular um relatório de pedidos filtrados por período

# Lista com pedidos realizados durante o mês (exemplo com 10 pedidos)

pedidos = ['Pedido 1001',
           'Pedido 1002',
           'Pedido 1003',
           'Pedido 1004',
           'Pedido 1005',
           'Pedido 1006',
           'Pedido 1007',
           'Pedido 1008',
           'Pedido 1009',
           'Pedido 1010']

# escreva seu código abaixo
# 1o passo - listas vazias para separa os pedidos pares e ímpares
pares = []
impares = []

# 2o passo - Laço(FOR) que percorre cada item da lista 'pedidos'
# tradução: para cada pedido dentro da lista de pedidos, execute o código dentro do FOR
for pedido in pedidos:
    #pegar o número do pedido(ultimos 4 digitos) e converter em número inteiro
    numero = int(pedido [-4:])
    
    #verificar se o resto da divisão é par ou impar
    if numero % 2 == 0:
        pares.append(pedido) #adicionar o número na lista de pares
    else:
        impares.append(pedido) #adicionar o número na lista de impares
        

# todos os pedidos
print('\nTodos os pedidos do mês:')
print(pedidos)

# os 5 últimos pedidos
print('\nÚltimos 5 pedidos realizados:')
print(pedidos[-5:])

# pedidos da segunda semana (índices 5 até 8)
print('\nPedidos da segunda semana do mês')
print(pedidos[5:9])

# 3 primeiros pedidos
print('\nExibe os 3 primeiros pedidos:')
print(pedidos[:3])

# pedidos PARES
print('\nPedidos pares:')
print(pares)

# pedidos ÍMPARES
print('\nPedidos Ímpares:')
print(impares)























