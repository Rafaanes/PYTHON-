'''
    Pede-se cadastro de senha

    ENTRADAS:
        senha cadastrada
        senha entrada
    
    PROCESSAMENTO:
        enquanto a senha cadastrada for diferente 
        da senha de entrada continue e verificação(Looping)

    SAIDA:
        quando a senha de cadastrada for igual a senha de entrada
        exibir "Acesso Permitido"

'''
# Escreva seu código aqui
# 1o passo - validar a senha - Entradas
senha_cadastrada = input('Cadastrar uma senha: ').strip()
senha_entrada = ''
contador = 1
permite_acesso = True

if senha_cadastrada == '':
    print('Digite uma senha válida! O programa será encerrado...')
    exit()

# 2o passo - validar
# enquanto senha cadastrada for diferente da senha entrada, 
# continue o Looping(While)
# != significa operador para validar se as variáveis são diferentes
while senha_cadastrada != senha_entrada:
    senha_entrada = input('Digite a senha para entrar: ')
    
    if contador == 3 and senha_cadastrada != senha_entrada:
        print(f'Foram realizadas: {contador} tentativas, acesso bloqueado')
        
        permite_acesso = False
        break
    #contador = contador + 1(didático)
    contador += 1 
    
# 3o passo - permitir acesso
if permite_acesso == True:
    print('Acesso permitido')
























































































