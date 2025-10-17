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

'Escreva seu código abaixo'

# 1o passo - ENTRADAS


menu = int (input('''
'Controle de Pagamento PAGA BEM!
                                  
[1] Cartão de crédito.
[2] Boleto bancário.
[3] Pix.
[4] Dinheiro

Digie o número do método de pagamento:
'''))
if menu <1 or menu >4:
    print('Opção inválida! O programa será encerrado.')
    exit()
match menu:
    case 1:
        print(f'Você escolheu pagamento com Cartão de crédito. Pagamento aprovado!')
    case 2:
        print(f'Você escolheu pagamento com Boleto bancário. Pagamento em processamento...')
    case 3:
        print(f'Você escolheu pagamento com PIX. Pagamento realizado com sucesso!')
    case 4:
        print(f'Você escolheu pagamento em Dinheiro. Pagamento confirmado!')
        
    

    





























