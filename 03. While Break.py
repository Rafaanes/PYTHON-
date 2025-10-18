'''
    While com Break
    while True: >>> este laço será executado enquanto 
    não encontrar o Break pelo caminho.
    Break >>> Condição de parada/encerramento(stop) de um loop. 

'''
# Escreva seu código aqui
while True: #enquanto verdadeiro
    
    menu = int(input('''
[1] CADASTRAR
[2] SAIR
Digite a opção:               
'''))

    match menu:
        case 1: 
            nome = input('Digite o nome: ')
        case 2:
            print('Obrigado e volte sempre!')
            break
        case _:
            print('Opção inválida')
           

print('Sai do While (looping)')
print('Fim do programa....')































