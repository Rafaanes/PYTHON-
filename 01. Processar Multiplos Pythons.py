import os
import subprocess

# item 1 - localizar a pasta dos arquivos
# local onde encontram-se todos os .py a serem processados
pasta_scripts = r'C:\Rafaélla Sena - Python\Python 2\Python 2 - Clarify\Aluno\Aula_06\Aula\Processar - Thread'

# item 2 - cria uma lista com todos os arquivos da pasta
# que terminam com '.py'
arquivos_py = [diretorio for diretorio in os.listdir(pasta_scripts) if diretorio.endswith('.py')]

# item 3 - para cada arquivo .py encontrado na lista...
for arquivo in arquivos_py:
    #juntar o caminho da pasta com o nome do arquivo para ter o caminho completo
    caminho_completo = os.path.join(pasta_scripts, arquivo)

    #mostra na tela qual o arquivo está sendo executado
    print(f'\n Executando o arquivo Python: {arquivo}')

    #executa o arquivo usando o caminho do sistema
    subprocess.run([os.sys.executable, caminho_completo], check=True)

#fim do processamento
print('\nTodos os scripts(programas) form executados!')





