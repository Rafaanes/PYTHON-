'''
Pede-se:
===========


   VARIAVEIS
   =========
      cod_produto = (numérico) 
      descricao = (texto) 
      preco = (valor decimal)
      ativo = (TRUE)
   
   ENTRADA
   =======
      cod_produto = faça a variável receber somente números
                  ('Digite o código: ') 

      descricao = faça a variável receber somente texto 
                  ('Digite o nome: ') 

      preco = faça a variável receber somente valor decimal
               ('Digite o preço: ')

      produto ativo = faça a variável receber somente boleano(TRUE) verdadeiro


   SAÍDA
   =====
   1) exibir os valores digitados em cada variável (print)
   2) se a variavel produto_ativo for igual TRUE então, 
         exibir 'Produto ativo'
      senão 
         exibir 'Produto inativo'
    
'''

# Bibliotecas do Python:
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/library/stdtypes.html#str.format

# Conforme todo material que você executou com o professor
# até aqui, chegou sua vez colocar em prática todo conhecimento.

# Leia atentamente o enunciado acima e aplique a solução !
# Boa sorte !
'Escreva seu código abaixo'

cod_produto = int (input('Digite o código: '))
descricao = input('Digite o nome: ')
preco = float (input('Digite o preço: '))
ativo = True

print (f'Código do produto: {cod_produto}')
print (f'Descrição: {descricao}')
print (f'Preço: {preco}')

if ativo == True:
   print ('Produto ativo')
else:
   print ('Produto inativo')






















