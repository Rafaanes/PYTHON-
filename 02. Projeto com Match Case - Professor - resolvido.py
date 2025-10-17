'''
    Cenário:
    =======
    Controle de Pagamento empresa PAGA BEM

    Neste exemplo, o usuário escolhe um método de pagamento, 
    e o sistema responde com uma mensagem adequada.


    ENTRADAS
    ========
    exibir: Controle de Pagamento
    exibir: Escolha o método de pagamento:
    
    exibir: 1 - Cartão de Crédito
    exibir: 2 - Boleto Bancário
    exibir: 3 - Pix
    exibir: 4 - Dinheiro

    pagamento = exibir o texto 'Digite o número do método de pagamento:'

    PROCESSAMENTO / MACTH CASE
    ==========================
    Quando método = 1
        exibir = Você escolheu pagamento com Cartão de Crédito. Pagamento aprovado!
    Quando método = 2
        exibir = Você escolheu pagamento com Boleto Bancário. Pagamento em processamento...
    Quando método = 3
        exibir = Você escolheu pagamento com Pix. Pagamento realizado com sucesso!
    Quando método = 4
        exibir = Você escolheu pagamento em Dinheiro. Pagamento confirmado!
    Quando o método de pagamento for diferente do escolhido
        exibir = Pagamento inválido. Tente novamente!


'''

# Escreva seu código abaixo
# -------------------------

# 1o passo - ENTRADAS

menu = int(input('''
[1] Cartão de Crédito
[2] Boleto Bancário
[3] Pix
[4] Dinheiro
Escolha o método de pagamento: '''))

if menu < 1 or menu > 4:    
    print('Opção inválida... Pagamento inválido. Tente novamente!')
    exit() # encerra a leitura do código aqui / stop o programa

# 2o passo - MENU
match menu:
    case 1:
        print('Você escolheu pagamento com Cartão de Crédito. Pagamento aprovado!')

    case 2:
        print('Você escolheu pagamento com Boleto Bancário. Pagamento em processamento.')

    case 3:
        print('Você escolheu pagamento com Pix. Pagamento realizado com sucesso!')

    case 4:
        print('Você escolheu pagamento em Dinheiro. Pagamento confirmado!')







