
'''

    RANDOM
    ======
    Essa biblioteca é muito interessante quando precisamos 
    trabalhar com dados aleatórios. Sendo uma ferramenta muito
    interessante na área de estatística para simular valores aleatórios

    https://docs.python.org/pt-br/3/library/random.html

'''

# escreva seu código aqui

# 1o passo - chamar a lib(biblioteca)
import random


print('Atribuição de Clientes e Representantes de Vendas')

representante_1 = 'Carlos'
representante_2 = 'Ana'
representante_3 = 'Júlia'
representante_4 = 'Lucas'
representante_5 = 'Fernanda'

# 2o passo - definir os clientes
cliente_1 = 'Vaio'
cliente_2 = 'Dell'
cliente_3 = 'Microsoft'
cliente_4 = 'Apple'
cliente_5 = 'Meta'

# 3o passo - sorteando o representante de vendas
# randint() = números inteiros

representante_escolhido = random.randint (1,5)
print (f'Número aleatório do sistema representante: {representante_escolhido}')


# 4o passo - sorteando o cliente
cliente_escolhido = random.randint(1,5)
print(f'Número aleatório do sistema cliente: {cliente_escolhido}')



# 5o passo - atribuir o representante e o cliente com base no número 
# sorteado
match representante_escolhido:
    case 1: 
        representante = representante_1
    case 2: 
        representante = representante_2
    case 3: 
        representante = representante_3
    case 4:
        representante = representante_4
    case 5:
        representante = representante_5
        
        
match cliente_escolhido:
    case 1:
        cliente = cliente_1
    case 2:
        cliente = cliente_2
    case 3:
        cliente = cliente_3
    case 4:
        cliente = cliente_4
    case 5:
        cliente = cliente_5
        
print (f' O(a) representante {representante} foi designado(a) para a cliente {cliente}')




























































