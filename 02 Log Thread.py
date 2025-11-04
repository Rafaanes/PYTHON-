import os
from datetime import datetime #registrar data e hora no log
import getpass #pegar o usuário do windowns 
import subprocess


# ============================================
# CONFIGURAÇÃO
# ============================================
# item 1 - localizar a pasta dos arquivos
# local onde encontram-se todos os .py a serem processados
pasta_scripts = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_06\Aula\Processar - Thread'
pasta_log = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_06\Aula'

# Escolha do tipo de log:
# True  = criar um arquivo novo a cada execução
# False = usar sempre o mesmo arquivo de log
log_por_execucao = False

# Usuário que executou
usuario = getpass.getuser()
#gerenv = Enviroment é uma variavel de ambiente do Windowns
nome_computador = os.getenv('COMPUTERNAME')

# ============================================
# Definir arquivo de log
# ============================================
if log_por_execucao: #se for verdadeito
    data_hora_atual = datetime.now().strftime('%d_%m_%Y_%Hh_%Mm_%Ss')
    arquivo_log = os.path.join(pasta_log, f'log_execucao_{data_hora_atual}.txt')
else:
    arquivo_log = os.path.join(pasta_log, 'log_execucao.txt')

# ============================================
# Função para registrar mensagens no log
# ============================================
def registrar_log(mensagem):
    with open(arquivo_log, 'a', encoding = 'utf-8') as log:
        data_hora =  datetime.now().strftime('%d/%m/%Y /%H:%M:%S')
        log.write(f'[{data_hora}] {mensagem}\n') 

# ============================================
# Início da execução — registra no log
# ============================================
registrar_log('=== Início da execução dos Scripts ===')
registrar_log(f'Usuário/Login: {usuario} | Computador: {nome_computador}')

# ============================================
# item 2 - cria uma lista com todos os arquivos da pasta
# que terminam com '.py'
# ============================================
arquivos_py = [pasta_subpasta for pasta_subpasta in os.listdir(pasta_scripts) if pasta_subpasta.endswith('.py')]

# ============================================
# item 3 - para cada arquivo .py encontrado na lista...
# ============================================
for arquivo in arquivos_py:
    #juntar o caminho da pasta com o nome do arquivo para ter o caminho completo
    caminho_completo = os.path.join(pasta_scripts, arquivo)

    #mostra na tela qual arquivo está sendo executado
    print(f'\nExecutando: {arquivo}')

    registrar_log(f'Executando Script: {arquivo}')

    #executa o arquivo usando o caminho do sistema
    retorno = subprocess.run([os.sys.executable, caminho_completo], check=True)

    #verifica se a execução foi bem sucedida
    if retorno == 0:
        registrar_log(f'Sucesso ao executar: {arquivo}')
    else:
        registrar_log(f'ERRO ao executar: {arquivo} Código de retorno: retorno: {retorno}')

# ============================================
# Depois que todos os arquivos foram executados, mostra uma mensagem final
# ============================================
print('\nTodos os scripts foram executados')
registrar_log('=== Fim da execução dos Scripts === \n')














