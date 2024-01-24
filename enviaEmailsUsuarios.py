import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import os
from mensagem import corpoEmail
import pandas as pd


# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 25
smtp_user = 'alexandre.bcc7@gmail'
smtp_password = 'ydhmdbkxwtxttqwp'

destinatarios = pd.read_excel("./Base de Dados - Usuários.xlsx", header=0)

# Construir e enviar e-mails personalizados
for destinatario in range(0,len(destinatarios.iloc[:,0])):
    # Configurar mensagem
    mensagem = MIMEMultipart()
    mensagem['From'] = smtp_user
    mensagem['To'] = destinatarios.EMAIL[destinatario]
    mensagem['Subject'] = 'Ferramenta de levantamento de compras institucionais de TIC da UFC'

    # Corpo do e-mail em formato HTML
    emailUnidade = destinatarios.EMAIL[destinatario]
    nomeGestor = destinatarios.NOME[destinatario].split()[0]
    corpo_email = corpoEmail(emailUnidade,nomeGestor)

    # Adicionar corpo do e-mail à mensagem
    mensagem.attach(MIMEText(corpo_email, 'html'))

  
    caminho_do_pdf = 'ManuadoUsuarioPedidosTIC.pdf'
    with open(caminho_do_pdf, 'rb') as anexo_pdf:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(anexo_pdf.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{caminho_do_pdf}"')
        mensagem.attach(part)
    

    # Conectar ao servidor SMTP e enviar e-mail
    # Conectar ao servidor SMTP do Gmail e enviar e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, destinatarios.EMAIL[destinatario], mensagem.as_string())

       
    
    print("enviado para "+str(destinatarios.EMAIL[destinatario]))


print('E-mails enviados com sucesso!')

