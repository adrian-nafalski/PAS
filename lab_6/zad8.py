import smtplib
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

# dane serwera SMTP
smtp_server = "smtp.interia.pl"
smtp_port = 587


def main():
    smtp_username = input("Podaj login SMTP: ")
    smtp_password = input("Podaj hasło SMTP: ")

    # dane wiadomości e-mail
    from_addr = input("Podaj adres nadawcy: ")
    to_addrs = input("Podaj adresy odbiorców, oddzielone przecinkami: ").split(',')
    subject = input("Podaj temat wiadomości: ")
    body = input("Podaj treść wiadomości: ")
    attachment_path = input("Podaj ścieżkę do pliku z załącznikiem: ")

    # przygotowanie wiadomości e-mail
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = COMMASPACE.join(to_addrs)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # dodanie załącznika
    if os.path.isfile(attachment_path):
        with open(attachment_path, 'rb') as f:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(f.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition',
                                  'attachment',
                                  filename=os.path.basename(attachment_path))
            msg.attach(attachment)
    else:
        print("Plik z załącznikiem nie został odnaleziony")

    # wysłanie wiadomości e-mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_addr, to_addrs, msg.as_string())
        server.quit()
        print("Wiadomość e-mail została wysłana!")
    except Exception as e:
        print("Wystąpił błąd podczas wysyłania wiadomości e-mail: ", str(e))


if __name__ == "__main__":
    main()
