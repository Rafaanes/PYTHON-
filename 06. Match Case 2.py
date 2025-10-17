"""
    Estrutura condicionais mais utilizada em menus,
    funciona semelhante ao escolha Caso do portugol
    e switch case no java por exemplo...
"""
# Calculadora

# Escreva seu código aqui

menu = int (input('''
[1] SOMAR
[2] SUBTRAIR   
[3]MULTIPLICAR      
[4]DIVIDIR

Digite o número para realizar os cálculos:
               
'''))

#verificação se o usuário digitou uma opção correta para realizar os cálculos
if menu >= 1 and menu <= 4:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
else:
    print ('Opcão inválida! O programa será encerrado!')
    exit() #encerra a leitura do código aqui/stop

match menu:
    
    case 1:
        print(f'Somar os valores, temos {n1 + n2}')
    
    case 2: 
        if n1 >= n2:
            print(f'Subtrair os valores, temos: {n1-n2}')
        else:
            print(f'Subtrair os valores, temos: {n2-n1}')
            
    case 3:
        print(f'Multiplicar os valores, temos: {n1*n2}')
        
    case 4: 
        print(f'Dividir os valores, temos: {n1/n2}')

























