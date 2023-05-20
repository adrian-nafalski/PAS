"""
Zadanie 2
"""

import imaplib

# Dane logowania do serwera IMAP
IMAP_SERVER = input("Podaj adres serwera: ")
EMAIL = input("Podaj e-mail: ")
PASSWORD = input("Podaj hasło: ")


def main():
    # Nawiązanie połączenia z serwerem IMAP
    imap = imaplib.IMAP4_SSL(IMAP_SERVER)

    # Logowanie do konta email
    imap.login(EMAIL, PASSWORD)

    # Wybór skrzynki odbiorczej (Inbox)
    imap.select("Inbox")

    # Pobranie informacji o skrzynce odbiorczej
    status, response = imap.status("Inbox", "(MESSAGES UNSEEN)")

    if status == "OK":
        # Parsowanie informacji o liczbie wiadomości
        messages_info = response[0].split()
        num_messages = int(messages_info[1])
        num_unseen = int(messages_info[3])

        # Wyświetlanie informacji
        print(f"Liczba wiadomości: {num_messages}")
        print(f"Liczba nieprzeczytanych: {num_unseen}")

    # Zamknięcie połączenia z serwerem IMAP
    imap.logout()


if __name__ == "__main__":
    main()
