""" 
SETs
====
    Não ordenadas
    Mutáveis
    não permitem itens repetidos
    

 # Analise as cidades (cada pessoa que entrou colocou a cidade de nascimento)

 """

# Lista com cidades (com duplicadas)
cidades = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
           'Salvador', 'Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
           'Salvador', 'São Paulo', 'São Paulo', 'São Paulo', 'Juiz de Fora',
           'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
           'Juiz de Fora', 'Petrolina', 'Salvador', 'Rio de Janeiro',
           'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
           'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
           'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo', 'Rio de Janeiro',
           'São Paulo', 'Rio de Janeiro', 'São Paulo', 'São Paulo']

# Usando set para remover duplicadas
cidades_sem_duplicadas = set(cidades)

# Exibindo o resultado
print(cidades_sem_duplicadas)





