'''
# ==========================================================
# OBJETIVO DESTE SCRIPT:
# Enviar um e-mail com corpo em HTML e anexo usando o GMAIL
# ==========================================================

Resumo
======
Provedor: é a empresa onde você tem o e-mail (ex: Gmail, Outlook, Yahoo, UOL).

Servidor SMTP: é o endereço usado para enviar e-mails pelo 
provedor (ex: smtp.gmail.com).

Porta: é o “canal de comunicação” usado para conectar com o servidor.

587 → conexão segura (mais usada e recomendada)

465 → conexão segura antiga (SSL direto)

25 → padrão antigo, muitas vezes bloqueada



Servidores SMTP mais comuns
===========================

Provedor	                Servidor SMTP	        Porta
--------                    -------------           -----
Gmail	                    smtp.gmail.com	        587
Outlook / Hotmail / Live	smtp.office365.com	    587
Yahoo Mail	                smtp.mail.yahoo.com	    587
iCloud (Apple)	            smtp.mail.me.com	    587
Zoho Mail	                smtp.zoho.com	        587
Proton Mail (via Bridge)	127.0.0.1	            1025
UOL	                        smtps.uol.com.br	    465
Terra	                    smtp.terra.com.br	    587
BOL	                        smtps.bol.com.br	    465
Globo / GMail Globo.com	    smtp.globo.com	        465
R7 Mail	                    smtp.r7.com	            587
IG Mail	                    smtp.ig.com.br	        587
SendGrid	                smtp.sendgrid.net	    587
Mailgun	                    smtp.mailgun.org	    587
Brevo (ex-Sendinblue)	    smtp-relay.brevo.com	587
Postmark	                smtp.postmarkapp.com	587


Notas rápidas
=============
Porta 587 (STARTTLS) → a mais usada hoje (recomendada).

Porta 465 (SSL) → conexão segura direta (ainda usada em 
provedores antigos como UOL, BOL, Globo).

Porta 25 → tradicional, mas geralmente bloqueada por 
provedores residenciais (use apenas em redes corporativas).

'''



# ==========================================================
# 1º passo - Importação da biblioteca "smtplib"
# ----------------------------------------------------------
# Esta biblioteca já vem com o Python.
# Ela é usada para enviar e-mails utilizando o protocolo SMTP
# (Simple Mail Transfer Protocol).
# É o protocolo padrão usado para enviar mensagens de e-mail
# através de servidores como o Gmail.
# ==========================================================
import smtplib


# ==========================================================
# 2º passo - Estas importações são da biblioteca "email.mime"
# ----------------------------------------------------------
# MIME significa "Multipurpose Internet Mail Extensions",
# que é um formato padrão para e-mails com texto, HTML e anexos.
# 
# - MIMEText: usado para criar o corpo do e-mail (texto ou HTML)
# - MIMEMultipart: permite que o e-mail tenha várias partes
#   (exemplo: texto + anexo)
# ==========================================================
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# ==========================================================
# 3º passo - MIMEBase é usado quando precisamos enviar arquivos anexados.
# Com ele conseguimos ler o arquivo, codificá-lo em formato
# que possa ser transmitido por e-mail e incluir no corpo.
# ==========================================================
from email.mime.base import MIMEBase

# ==========================================================
# 4º passo - O módulo "encoders" é usado para converter (codificar)
# o arquivo em base64, formato necessário para que o anexo
# possa ser transmitido por e-mail sem se corromper.
# ==========================================================
from email import encoders


# ==========================================================
# 5º passo - O módulo "os" (Operating System) é uma biblioteca que
# permite interagir com o sistema operacional (Windows, Linux).
# Aqui ele é usado para pegar apenas o nome do arquivo
# sem precisar do caminho completo.
# ==========================================================
import os


# ==========================================================
# 6º passo - CONFIGURAÇÕES BÁSICAS DO E-MAIL
# ----------------------------------------------------------
# Aqui colocamos o remetente (quem envia) e a senha de app.
# Importante: a senha é a "senha de aplicativo" do Gmail,
# e não a senha normal da sua conta Google.
# Para gerar: Conta Google → Segurança → Senhas de app.
# ==========================================================
seu_email = 'rafaellasena200@gmail.com'
sua_senha = 'ugab nyrs dtci wipz' # senha APP

# ==========================================================
# 7º passo - Criamos um objeto "mensagem" do tipo MIMEMultipart.
# Este objeto servirá para "montar" o e-mail,
# juntando corpo, cabeçalhos e anexos.
# ==========================================================
mensagem = MIMEMultipart()


# ==========================================================
# 8º passo - Definição dos cabeçalhos do e-mail:
# - From: quem envia
# - To: para quem vai
# - Cc: cópia (aparece para todos)
# - Bcc: cópia oculta (não aparece para os demais)
# - Subject: assunto do e-mail
# ==========================================================
mensagem ['FROM'] = seu_email
mensagem['TO'] = 'rafaanes1@hotmail.com'
mensagem['Cc'] = 'marcelopfsena@gmail.com'
mensagem['Bcc'] = 'rafaanes.1@hotmail.com'
mensagem['Subject'] = 'Teste com GMAIL, Python e Anexo'

# ==========================================================
# 9º passo - CORPO DO E-MAIL EM HTML
# ----------------------------------------------------------
# O corpo pode ser em texto simples ou HTML.
# HTML permite formatação: títulos, negrito, parágrafos etc.
# Aqui usamos um <h1> e <b> para demonstrar.
# ==========================================================
corpo_email_html = '''
<html>
    <body>
        <h1> Olá, este é um email de teste <b> PYTHON</b>
    </body>
</html>
'''


# ==========================================================
# 10º passo - "attach" adiciona o corpo HTML dentro da mensagem.
# O parâmetro 'html' informa que o conteúdo é HTML
# e não texto simples.
# ==========================================================
mensagem.attach(MIMEText(corpo_email_html, 'html'))


# ==========================================================
# 11º passo - CAMINHO DO ARQUIVO A SER ANEXADO
# ----------------------------------------------------------
# O prefixo "r" antes das aspas significa "raw string"
# (string bruta). Ele faz o Python ler o caminho exatamente
# como está, sem tentar interpretar as barras invertidas.
# Exemplo: sem o "r", o Python poderia entender "\n" como nova linha.
# ==========================================================
caminho_arquivo = r'C:\Python\Teste Python.docx'


# ==========================================================
# BLOCO TRY: usado para tratar erros durante a execução.
# Se algo der errado, o Python "pula" para o bloco "except"
# correspondente e mostra uma mensagem amigável.
# ==========================================================

# *** PROFESSOR SÓ COLOCAR O TRY, APÓS TESTAR COM A TURMA,
# *** SENÃO PROFESSOR VOCÊ NÃO VAI CONSEGUIR DESCOBRIR ONDE DEU ERRO
# *** NO CODIGO DA TURMA


# 12 º passo - Abre o arquivo especificado em "caminho_arquivo" no modo binário ('rb')
# - 'r' significa leitura
# - 'b' significa binário (necessário para arquivos que não são texto, como .docx, .pdf, imagens)
# O "with" garante que o arquivo será fechado automaticamente ao sair do bloco
with open(caminho_arquivo, 'rb') as anexo:
    
    # Cria um objeto MIMEBase, que representa uma "parte" do e-mail
    # Neste caso, a parte que será anexada
    # - 'application' indica que é um arquivo de aplicação (conteúdo genérico)
    # - 'octet-strem' (geralmente escrito 'octet-stream') indica que o conteúdo é um fluxo de bytes
    #   ou seja, qualquer tipo de arquivo binário
    parte = MIMEBase('application', 'octet-strem')
    
    # Lê todos os bytes do arquivo aberto e coloca dentro do objeto "parte"
    # - anexo.read() retorna o conteúdo do arquivo em bytes
    # - set_payload() define esses bytes como o conteúdo da parte MIME
    parte.set_payload(anexo.read())

# ----------------------------------------------------------
# 13º passo - Codifica o conteúdo da parte MIME em base64
# - Necessário para anexos binários (PDF, DOCX, imagens)
# - E-mails foram projetados para texto ASCII, não aceitam bytes brutos
# - encode_base64 transforma os bytes do arquivo em texto seguro para envio
# - Também adiciona internamente o cabeçalho 'Content-Transfer-Encoding: base64'
# ----------------------------------------------------------
encoders.encode_base64(parte)

# ----------------------------------------------------------
# 14º passo - Extrai somente o nome do arquivo (sem o caminho completo).
# Exemplo: de "C:\PYTHON\Teste Python.docx" fica apenas "Teste Python.docx"
# ----------------------------------------------------------
nome_arquivo = os.path.basename(caminho_arquivo)

# ----------------------------------------------------------
# 15º passo - Adiciona um cabeçalho à parte MIME informando que é um anexo
# - 'Content-Disposition' é o nome do cabeçalho que indica como o conteúdo deve ser exibido
# - 'attachment' diz que esta parte é um arquivo anexo, não parte do corpo do e-mail
# - 'filename="{nome_arquivo}"' especifica o nome que o anexo terá no e-mail do destinatário
#   Exemplo: se nome_arquivo = 'Teste Python.docx', o destinatário verá exatamente esse nome
# - Esse cabeçalho é essencial para que os clientes de e-mail (Outlook, Gmail, etc.)
#   reconheçam a parte como um arquivo que pode ser baixado ou aberto
# ----------------------------------------------------------
parte.add_header('Content-Disposition', f'attachment;filename = {nome_arquivo}"')

# ----------------------------------------------------------
# 16º passo - Adiciona (anexa) o arquivo à mensagem.
# ----------------------------------------------------------
mensagem.attach(parte)


# ==========================================================
# 17º passo - DESTINATÁRIOS
# ----------------------------------------------------------
# Aqui o código junta todos os tipos de destinatários
# (To, Cc e Bcc) em uma única lista.
# O método split(',') divide o texto por vírgula.
# Assim, podemos enviar para várias pessoas de uma vez.
# ==========================================================
destinatarios = mensagem['TO'].split(',') + mensagem['Cc'].split(',') + mensagem['Bcc'].split(',')


# ==========================================================
# 18º passo - ENVIO DO E-MAIL
# ----------------------------------------------------------
# Aqui ocorre a conexão com o servidor do Gmail.
# Endereço: smtp.gmail.com
# Porta: 587 (usada para STARTTLS, conexão segura)
# ==========================================================
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    # ----------------------------------------------------------
    # Inicia a conexão segura (criptografada)
    # ----------------------------------------------------------
    server.starttls()

    # ----------------------------------------------------------
    # Faz o login usando o e-mail e a senha APP
    # ----------------------------------------------------------
    server.login(seu_email,sua_senha)

    # ----------------------------------------------------------
    # Envia o e-mail:
    # - remetente
    # - lista de destinatários
    # - conteúdo convertido em string
    # ----------------------------------------------------------
    server.sendmail(seu_email, destinatarios, mensagem.as_string())

# ----------------------------------------------------------
# 19º passo - Caso tudo dê certo, aparece esta mensagem no console.
# ----------------------------------------------------------
print('E-mail foi enviado com sucesso!!')





































