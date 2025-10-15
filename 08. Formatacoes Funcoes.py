# 1) .upper() = Transformar em letras maiúsculas
maiuscula = "clarify treinamentos"
print('maiuscula: ' + maiuscula.upper()) 
# Resultado: CLARIFY TREINAMENTOS


# 2) .lower() = Transformar em letras minúsculas
minuscula = "CLARIFY TREINAMENTOS"
print('minuscula: ' + minuscula.lower()) 
# Resultado: clarify treinamentos


# 3) .capitalize() = Primeira letra maiúscula
'''
Use o método .capitalize() para colocar 
apenas a primeira letra em maiúscula e o 
restante em minúsculas.
'''
primeira_letra_maiuscula = "clarify treinamentos"
print(' .capitalize(): ' + primeira_letra_maiuscula.capitalize()) 
# Resultado: Clarify treinamentos


# 4) .title() = Primeira letra de cada palavra maiúscula
'''
Use o método .title() para colocar a primeira 
letra de cada palavra em maiúscula.
'''
primeira_letra_de_cada_palavra_maiuscula = "clarify treinamentos"
print('primeira letra de cada palavra em maiúscula .title(): ' + primeira_letra_de_cada_palavra_maiuscula.title()) 
# Resultado: Clarify Treinamentos


# 5) .strip() = Remover espaços do início e do fim
remover_espacos = "   Clarify Python 1!   "
print('.strip remover espaços ' + remover_espacos.strip()) 
# Resultado = "Clarify Python 1!"


# 6) .replace() = substituir(texto antigo, texto novo)
substituir = "Clarify Python 1"
print('substituir .replace() ' + substituir.replace('Python 1', 'Python 2'))
# Resultado: Clarify Python 2


# 7) .find() = é usado para localizar a posição (índice) 
#              de um texto e começa a contar sempre o índice 0
localizar1 = "Hoje é um ótimo dia para aprender Python"
print(' .find ' + str(localizar1.find('ótimo')))
# Resultado: 10 ("ótimo" está na décima posição)



localizar2 = "Clarify Treinamentos"
print('.find ' + str(localizar2.find('i', 11)))
# Resultado: 11 ("i" está na décima primeira posição)



















