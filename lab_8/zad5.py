"""
Zadanie 5
"""

import imaplib

# Dane serwera IMAP
SERVER_PORT = 993
SERVER_ADDRESS = input("Podaj adres serwera: ")
USERNAME = input("Podaj nazwę użytkownika: ")
PASSWORD = input("Podaj hasło: ")


def main():
    # Wybór numeru wiadomości do usunięcia
    MESSAGE_NUMBER = 1

    # Tworzenie połączenia z serwerem IMAP
    imap_server = imaplib.IMAP4_SSL(SERVER_ADDRESS, SERVER_PORT)

    # Logowanie
    imap_server.login(USERNAME, PASSWORD)

    # Wybór skrzynki odbiorczej (INBOX)
    imap_server.select("INBOX")

    # Pobieranie listy numerów wiadomości w skrzynce odbiorczej
    _, message_numbers = imap_server.search(None, "ALL")

    # Sprawdzenie poprawności numeru wybranej wiadomości
    if MESSAGE_NUMBER not in map(int, message_numbers[0].split()):
        print(f"Niepoprawny numer wiadomości: {MESSAGE_NUMBER}")
        imap_server.logout()
        exit()

    # Usuwanie wybranej wiadomości
    imap_server.store(str(MESSAGE_NUMBER), "+FLAGS", "\\Deleted")
    imap_server.expunge()

    # Wylogowanie i zamknięcie połączenia
    imap_server.logout()

    print(f"Wiadomość o numerze {MESSAGE_NUMBER} została usunięta.")


if __name__ == "__main__":
    main()
