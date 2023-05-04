"""
Zadanie 8
"""

import poplib


# Dane do połączenia z serwerem POP3
pop3_server = "pop.example.com"
pop3_port = 995
pop3_username = input("Username: ")
pop3_password = input("Password: ")


def main():
    # Nawiązanie połączenia z serwerem POP3
    pop3 = poplib.POP3_SSL(pop3_server, pop3_port)
    pop3.user(pop3_username)
    pop3.pass_(pop3_password)

    # Pobranie informacji o skrzynce pocztowej
    num_messages = len(pop3.list()[1])
    print(f"Ilość wiadomości w skrzynce: {num_messages}")
    print("Rozmiary wiadomości:")

    # Pobranie rozmiarów poszczególnych wiadomości
    for i in range(num_messages):
        response = pop3.retr(i+1)
        message_lines = response[1]
        message_size = sum(len(line) for line in message_lines)
        print(f"\tWiadomość {i+1}: {message_size} bajtów")

    # Zamknięcie połączenia z serwerem POP3
    pop3.quit()


if __name__ == "__main__":
    main()
    