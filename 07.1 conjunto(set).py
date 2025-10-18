'''
Resumo do Código de Tarefas com set
===================================

Objetivo:
=========
Gerenciar tarefas concluídas e pendentes usando conjuntos 
(set) para evitar duplicadas e facilitar operações entre elas.

Criação de conjuntos:
====================
    - tarefas_concluidas: tarefas já finalizadas.

    - tarefas_pendentes: tarefas ainda em andamento.

    - Duplicadas são automaticamente ignoradas pelo set

'''

# Criando um conjunto de tarefas concluídas
# Usamos set para garantir que não haja tarefas duplicadas
tarefas_concluidas = set([
    'Relatório financeiro',
    'Atualização do site',
    'Reunião com cliente',
    'Reunião com cliente',  # duplicada será ignorada
    'Pagamentos'
])

# Criando um conjunto de tarefas pendentes
tarefas_pendentes = set([
    'Desenvolvimento de novo sistema',
    'Relatório financeiro',
    'Treinamento de equipe',
    'Treinamento de equipe',  # duplicada será ignorada
    'Pagamentos'
])

# 1o passo - adicionar novas tarefas
# tarefa concluida recentemente


# 2o passo - nova tarefa pendente 


# 3o passo - remover tarefas de acordo com andamento do projeto



# 4o passo - exibir o estado atual das novas tarefas




# 5o passo - operações de conjuntos entre as tarefas
# | (pipe) é o operador de união: junta os dois conjuntos sem duplicadas



# 6o passo - tarefas em comum entre concluídas e pendentes
# & é o operador de interseção: mostra tarefas que estão em ambos os conjuntos



# 7o passo - diferença entre os conjuntos
# - o símbolo de menos é o operador de diferença: mostra tarefas que estão só
# em tarefas_concluidas e não em tarefas_pendentes











