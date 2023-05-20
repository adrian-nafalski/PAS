"""
Zadanie 3
"""

import imaplib

# Dane do logowania
IMAP_SERVER = input("Podaj adres serwera: ")
USERNAME = input("Podaj nazwę użytkownika: ")
PASSWORD = input("Podaj hasło: ")


def main():
    # Tworzenie połączenia z serwerem IMAP
    imap_connection = imaplib.IMAP4(IMAP_SERVER)

    # Logowanie
    imap_connection.login(USERNAME, PASSWORD)

    # Wybieranie wszystkich skrzynek
    status, mailbox_list = imap_connection.list()
    if status == "OK":
        total_messages = 0
        for mailbox in mailbox_list:
            # Pobieranie nazwy skrzynki
            _, mailbox_name = mailbox.decode().split(' "/" ')
            # Wybieranie skrzynki
            imap_connection.select(mailbox_name, readonly=True)
            # Pobieranie liczby wiadomości w skrzynce
            status, message_count = imap_connection.search(None, "ALL")
            if status == "OK":
                message_count = len(message_count[0].split())
                total_messages += message_count
                print(f"Liczba wiadomości w skrzynce {mailbox_name}: {message_count}")
        print(f"Liczba wiadomości we wszystkich skrzynkach: {total_messages}")

    # Zamykanie połączenia
    imap_connection.logout()


if __name__ == "__main__":
    main()
