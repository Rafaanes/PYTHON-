

""" 
CONTROLE DE ESTOQUE

ENUNCIADO:
==========
O programa solicita ao usuário a quantidade de itens em estoque
para diferentes produtos. Se o estoque for abaixo de um valor crítico, 
ele avisa o usuário. Em seguida, o programa verifica a quantidade 
de unidades vendidas de cada produto, calcula o preço final considerando
descontos e exibe um relatório. 


ENTRADAS
========
    Declaração de variáveis:

    estoque_minimo = 10  # Estoque mínimo crítico para os produtos
    desconto_grande = 0.2  # Desconto de 20% para vendas acima de 10 unidades
    desconto_pequeno = 0.1  # Desconto de 10% para vendas acima de 5 unidades
    preco_produto = 50  # Preço unitário do produto
    quantidade_estoque = 15  # Exemplo de quantidade inicial em estoque


LAÇO FOR
========

    O laço for é usado para processar 3 produtos diferentes. 
    Ele solicita o nome e a quantidade vendida de cada produto.
    
    Para cada produto, o programa verifica:

        produto_nome = entrada(Digite o nome do {x}º produto: ).LETRASMAIÚSCULAS

        Tratamento de Erro:
            quantidade_vendida = numérico(entrada(
                            Digite a quantidade vendida do produto: {produto_nome}))
        Exceção:
            mensagem: Você digitou uma quantidade inválida !
            Encerrar Looping aqui


        # Verificar se o estoque está abaixo do mínimo
        ==============================================
        Se a quantidade_estoque for menor que estoque_minimo então
            mensagem: Alerta! O estoque de {produto_nome} está abaixo do nível mínimo!
        else:
            mensagem: Estoque de {produto_nome} está suficiente

        # Calcular o preço com desconto baseado na quantidade vendida
        =============================================================
        (use: if, elif, else)
        Se as vendas forem acima de 10 unidades, um desconto de 20% é aplicado 
            mensagem: Desconto de 20% aplicado! Preço final do produto {?}: preço R${?}

        Se forem acima de 5 unidades, um desconto de 10% é aplicado
            mensagem: Desconto de 10% aplicado! Preço final do produto {?}: preço R${?}

        Se a quantidade vendida for 5 ou menos, nenhum desconto é aplicado
            mensagem: Sem desconto! Preço final do produto {?}: preço R${?}        
     
        
# ATUALIZAR O ESTOQUE APÓS A VENDA
==================================
    seu estoque menos(-=) a quantidade vendida
    
# RELATÓRIO DE ESTOQUE FINAL
============================

Se o estoque ficar abaixo do valor mínimo após a venda, o programa emite um alerta.
    mensagem: O estoque do produto: {?} está crítico após a venda!

"""


#1o passo - Entradas - variáveis

estoque_minimo = 10
desconto_grande = 0.2 #20%
desconto_pequeno = 0.1 #10%
preco_produto = 50 # preço unitário
qtde_estoque = 15 # qtde inicial

#2o passo - Laço(for) para verificar o estoque para diferente produtos (limite=3)

for produto_numero in range(1,4):    
    produto_nome = input(f'Digite o nome do produto número {produto_numero}: ').upper()
    
    #tratativa para identificar se a variável recebeu número 

    try: #tentar    
        qtde_vendida = int(input(f'Digite a quantidade do produto {produto_numero}: '))    
    except: #tratamento do erro
        print('Vocês digitou um número inválido!')
        break # encerra o for aqui(encerra a leitura)

    #ainda dentro do for
    #verificar se o estoque está abaixo do minimo
    if qtde_estoque < estoque_minimo:
        print(f'Alerta!! O estoque do produto {produto_nome} está no mínimo')
    else:
        print(f'Estoque do produto {produto_nome} está suficiente!')
        
    #calcular preço com desconto baseado na qtde vendida
    if qtde_vendida >= 10:
        preco_final = preco_produto * (1 - desconto_grande)
        print(f'Desconto de 20% aplicado!')
        print(f'Preço final do produto: {produto_nome}, valor R${preco_final: .2f}')
    elif qtde_vendida >= 5:
        preco_final = preco_produto * (1-desconto_pequeno)
        print(f'Desconto de 10% aplicado!')
        print(f'Preço final do produto: {produto_nome}, valor R${preco_final: .2f}')
    else:
        preco_final = preco_produto
        print('Sem desconto!')
        print(f'Produto {produto_nome}, valor R$ {preco_final: .2f}')

    #atualizar o estoque após a venda
    #qtde_estoque = qtde_estoque - qtde_vendida
    qtde_estoque -= qtde_vendida 

    #relatório de estoque final
    if qtde_estoque < estoque_minimo:
        print(f'O estoque do produto {produto_nome} está critíco após a venda!')
        
        
    
#Saindo do for
print('Fim do processamento...')

































































    


