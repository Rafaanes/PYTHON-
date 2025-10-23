# -----------------------------------------------------------
# PROGRAMA: mover_pasta.py
# OBJETIVO: Mover a pasta 'Arquivos_Hoje' para dentro da pasta
#           'Arquivos_Ja_Processados' em horário agendado.
# -----------------------------------------------------------

# 1) Importa bibliotecas da própria instalação do Python
#lib que tem funções para copiar, mover e apagar arquivos/pastas
import shutil

#lib os manipula arquivos e verifica se as pastas existem
import os
import time # horário agendado
import datetime #adição horário agendaddo

# 2) Defina aqui o caminho COMPLETO da pasta que você quer mover.
#    - r'texto' é para o Python entender que a barra \ não é 'caractere especial'.
#    - Troque o caminho abaixo pelo caminho REAL no seu computador.
origem = r'C:\Caminho\Arquivos_Hoje'


# 3) Caminho COMPLETO da pasta onde a pasta de origem será colocada.
#    Ou seja, o local onde você quer guardar a pasta movida.
destino = r'C:\Caminho\Arquivos_Ja_Processados'


# 4) Horario agendado
# Defina o horário de execução no formato "HH:MM" (24h)
hora_agendada = '21:00'

print(f'Aguardando o horário agendado: ({hora_agendada}) para mover a pasta...')

while True:
    agora = datetime.datetime.now().strftime('%H:%M')
    if agora == hora_agendada:
        print('Hora agendada atingida. Executando o script!')
        break
    
    time.sleep(10) #verifica a cada 10s o momento para a execução



# 5) Mover Pasta
# Antes de criar a pasta de destino e mover, verificamos se a pasta de origem existe.
if os.path.exists(origem):
    


    # a) Garante que a pasta de destino exista.
    #    - exist_ok=True: se a pasta já existir, não dá erro.
    #    - Se não existir, ele cria automaticamente.
    os.makedirs(destino, exist_ok = True)


    # b) Monta o caminho final onde a pasta vai parar.
    #    - os.path.basename(origem) pega só o último nome do caminho de origem
    #      (ex.: 'Arquivos_Hoje'), para manter esse nome dentro da nova pasta.
    #    - os.path.join junta o destino com esse nome.
    destino_final = os.path.join(destino, os.path.basename(origem))


    # c) Faz a movimentação real.
    #    - shutil.move faz o 'cortar e colar' de toda a pasta e conteúdo.
    shutil.move(origem, destino_final) #shutil.copy (ctrl c e v)


    # 7) Mensagem de confirmação para o usuário.
    print('Pasta movida com sucesso!')
else:
    # >>> ADIÇÃO PARA VERIFICAÇÃO <<<
    # Caso a pasta de origem não exista mais, evita erro e avisa o usuário.
    print('A pasta de origem não foi encontrada, nada para mover!')




