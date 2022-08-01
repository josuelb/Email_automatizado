import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

"""
hosts and ports: 
    outlook = "smtp.office365.com", "587"
    gmail = "smtp.gmail.com", "587"
"""


def enviar_email(login, password, to, quest_anex='N', cam_arquivo=None, filename=None):
    host = "smtp.office365.com"
    port = "587"

    #Startar o servidor SMTP
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()

    server.login(login, password)

    #Construção do email
    corpo = """
    <p>Olá, coloque aqui seu conteudo do email</p
    <p>Lembrando, estilo HTML</p>
    """

    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = to
    email_msg['Subject'] = "" #Qual é o assunto do email

    email_msg.attach(MIMEText(corpo, 'html')) #'html' ou 'plain'

    #Anexar arquivo
    if quest_anex == 'S':
        attchment = open(cam_arquivo, 'rb')

        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attchment.read())
        encoders.encode_base64(att)

        att.add_header('Content-Disposition', f'attachment; filename={filename}')
        attchment.close()

        email_msg.attach(att)

    #Enviar o email
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    server.quit()


login = str(input('Seu email: '))
password = str(input('Sua senha: '))
to = str(input('Para quem? '))
quest_anex = str(input('Deseja anexar um arquivo? [S/N] ')).upper()

if quest_anex == 'S':
    cam_arquivo = str(input('O caminho do arquivo: '))
    filename = str(input('Nome do arquivo: '))
elif quest_anex != 'S' or quest_anex != 'N':
    cam_arquivo = None
    filename = None

enviar_email(login, password, to, quest_anex, cam_arquivo, filename)
