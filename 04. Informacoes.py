
'''

TERMINAL
========
pip list = mostra todas as bibliotecas instaladas no ambiente Python atual, junto com suas versões

pip show nome_da_biblioteca = para saber se uma biblioteca já está instalada no seu ambiente Python,
exemplo: pip show pandas, se a biblioteca estiver instalada, ele mostrará informações 
como versão, local de instalação etc.

- como eu localizo as bibliotecas nativas do python ?
===================================================
help('modules') = para localizar as bibliotecas nativas (ou padrão) do Python.
Atenção: Esse comando pode demorar alguns segundos e mostrar também os 
módulos de terceiros (instalados com pip).
https://docs.python.org/3/library/

'''

# Como eu consigo ver o conteudo de cada biblioteca instalada ?
import datetime
print(dir(datetime))

# Se quiser saber só sobre uma classe específica ?

help(datetime.date)

# como eu faço para ver o conteúdo da biblioteca pandas(por exemplo) ?

import pandas as pd
print(dir(pd))

# Para ver a documentação de um item específico do pandas, use:
help(pd.DataFrame)

