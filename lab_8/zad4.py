"""
Zadanie 4
"""

import imaplib

# Dane do logowania
IMAP_SERVER = input("Podaj adres serwera: ")
USERNAME = input("Podaj nazwę użytkownika: ")
PASSWORD = input("Podaj hasło: ")


def main():
    # Połączenie z serwerem IMAP
    imap = imaplib.IMAP4_SSL(IMAP_SERVER)
    imap.login(USERNAME, PASSWORD)

    # Wybór skrzynki
    status, _ = imap.select("INBOX")
    if status != "OK":
        print("Błąd podczas wyboru skrzynki: ", status)
        exit()

    # Pobranie listy nieprzeczytanych wiadomości
    status, unseen_data = imap.search(None, "UNSEEN")
    if status != "OK":
        print("Błąd podczas pobierania nieprzeczytanych wiadomości: ", status)
        exit()

    # Sprawdzenie, czy są jakieś nieprzeczytane wiadomości
    message_ids = unseen_data[0].split()
    if not message_ids:
        print("Brak nieprzeczytanych wiadomości")
        exit()

    # Wyświetlenie treści nieprzeczytanych wiadomości
    for message_id in message_ids:
        status, message_data = imap.fetch(message_id, "(RFC822)")
        if status != "OK":
            print("Błąd podczas pobierania wiadomości: ", status)
            continue

        # Oznaczenie wiadomości jako przeczytanej
        imap.store(message_id, "+FLAGS", "\\Seen")

        # Wyświetlenie treści wiadomości
        print("Wiadomość ID:", message_id)
        print(message_data[0][1])

    # Zamknięcie połączenia
    imap.logout()


if __name__ == "__main__":
    main()
