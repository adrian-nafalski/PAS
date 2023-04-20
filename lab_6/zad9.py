"""
Zadanie 9
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Dane do logowania do serwera SMTP
smtp_server = "smtp.interia.pl"
smtp_port = 587


def main():
    smtp_username = input("Podaj login SMTP: ")
    smtp_password = input("Podaj hasło SMTP: ")

    # Adres nadawcy i odbiorcy
    from_address = input("Podaj adres nadawcy: ")
    to_address = input("Podaj adres odbiorcy: ")

    # Treść wiadomości
    subject = input("Podaj treść wiadomości: ")

    # Treść wiadomości w formacie HTML
    body = f'<html><body><h2>{subject}</h2><p><b>pogrubienie</b>, <i>pochylenie</i>, <u>podkreślenie</u></p><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png"></body></html>'

    # Tworzenie obiektu MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Dodanie tekstu HTML do wiadomości
    msg.attach(MIMEText(body, 'html'))

    # Dodanie obrazka do wiadomości
    with open("obrazek.jpg", "rb") as f:
        img_data = f.read()
        image = MIMEImage(img_data, name='obrazek.jpg')
        image.add_header('Content-ID', '<python-logo-master-v3-TM-flattened>')
        msg.attach(image)

    # Nawiązanie połączenia z serwerem SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Wysłanie wiadomości
    server.sendmail(from_address, to_address, msg.as_string())

    # Zamknięcie połączenia z serwerem SMTP
    server.quit()

    print("Wiadomość została wysłana!")


if __name__ == "__main__":
    main()
    