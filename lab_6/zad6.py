"""
Zadanie 6
"""

import smtplib

# Adres serwera ESMTP Interia.pl oraz port
smtp_server = "smtp.poczta.interia.pl"
port = 587


def main():
    # Dane logowania do serwera
    username = input("Podaj login: ")
    password = input("Podaj hasło: ")

    # Tworzenie obiektu serwera SMTP
    server = smtplib.SMTP(smtp_server, port)

    # Rozpoczęcie połączenia i logowanie do serwera
    server.ehlo()
    server.starttls()
    server.login(username, password)

    # Pobieranie danych od użytkownika
    from_address = input("Podaj adres nadawcy: ")
    to_address = input("Podaj adres odbiorcy: ")
    subject = input("Podaj temat wiadomości: ")
    message = input("Podaj treść wiadomości: ")

    # Formatowanie wiadomości
    msg = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{message}"

    # Wysyłanie wiadomości
    server.sendmail(from_address, to_address, msg)

    # Zamykanie połączenia z serwerem
    server.quit()

    print("Wiadomość została wysłana.")


if __name__ == "__main__":
    main()
