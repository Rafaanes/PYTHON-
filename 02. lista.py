                                                                                                                                                                                                                                                                                                                                                                                                                                                          
'''
    Cadastro de Clientes com Listas
    ===============================

    O que esse código deverá fazer:
    ------------------------------
    
    Usar duas listas para armazenar nomes de clientes e serviços.

    Exibir a relação cliente-serviço como em um sistema básico de atendimento.

    Mostrar como acessar dados por índice, simulando uma consulta.

    Desta maneira pode servir para empresas de TI, consultoria, contabilidade, 
    ou qualquer serviço recorrente.

'''
# 1o passo - identificar o número/tamanho da lista
clientes = ['Lucas Martins','Fernanda Costa','Joana Lima', 'Carlos Silva']

# 2o passo - lista com os serviços contratados
servico = ['Consultoria', 'Suporte técnico', 'Treinamento','Análise de dados']

# 3o passo - exibir todos os cientes e seus serviços
print('Clientes e serviços contratados')

# 4o passo - FOR
# len() para descobrir a qtde de itens dentro da lista

for posicao in range(len(clientes)):
    print(f'Cliente {clientes[posicao]}. Serviço {servico[posicao]}')













































































