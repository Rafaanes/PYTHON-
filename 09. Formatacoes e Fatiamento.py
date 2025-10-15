""" 
DEFINIÇÕES:
===========
    O Python utiliza a notação texto[:3] como parte do 
    conceito de slicing(fatiamento), que é uma forma 
    prática e poderosa de acessar partes de uma sequência, 
    como strings, listas ou tuplas. Essa abordagem é 
    utilizada porque é concisa, legível e flexível, 
    permitindo extrair subsequências sem a necessidade 
    de escrever loops ou funções adicionais.


 """

# 1) Obter os caracteres à esquerda (Left)
# Para pegar os primeiros n caracteres de uma string
# Pega os 3 primeiros caracteres conceito de slicing(fatiamento)
texto = 'Clarify'
left_part = texto[:3]
print(f'left_part texto[:3] = {left_part}')
# Resultado: Cla


# 2) Obter os caracteres à direita (Right)
# Para pegar os últimos n caracteres de uma string
# Pega os 3 últimos caracteres conceito de slicing(fatiamento)
# percorre o texto da "direita para esquerda"
texto = 'Clarify'
right_part = texto[-3:]
print(f'right_part texto[-3:] = {right_part}') 
# Resultado: ify


# 3) Obter caracteres no meio
# Use slicing para pegar uma parte específica da string
texto = 'Clarify'
middle_part = texto[2:5]  # Pega do índice 2 ao 4
print(f'middle_part  texto[2:5] = {middle_part}') 
# Resultado: ari

# 4) Remover espaços:
texto_com_espaco = '   Clarify   '

# Remove espaços de ambos os lados: "Clarify"
print(f'Remove espaços de ambos os lados .strip() = {texto_com_espaco.strip()}')
# Resultado: "Clarify"

# Remove espaços à Direita:
print(texto_com_espaco.rstrip())
print(f'Remove espaços à direita .rstrip() {texto_com_espaco.rstrip()}') 
# Resultado : '   Clarify'

# Remove espaços à Esquerda: 
print(f'Remove espaços de ambos os lados .lstrip() {texto_com_espaco.lstrip()}')
# Resultado: 'Clarify   '


# 5) Verifica se uma string começa ou termina com um texto específico
inicio_texto = "Aprender Python"
print(f'Texto inicia: startswith = {inicio_texto.startswith("Aprender")}')
# Resultado: True (verdadeiro,  o texto "inicia" com "Aprender")

texto_termina = 'Análise de dados Python 2'
print(f'Texto termina: endswith = {texto_termina.endswith("Python 2")}')
# Resultado: True (verdadeiro,  o texto "termina" com "Python 2")



