"""
Zadanie 10
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

    # Pobranie i wyświetlenie treści wszystkich wiadomości
    for i in range(num_messages):
        response = pop3.retr(i+1)
        message_lines = response[1]
        message_content = b'\n'.join(message_lines).decode("utf-8")
        print(f"\nTreść wiadomości {i+1}:\n{message_content}")

    # Zamknięcie połączenia z serwerem POP3
    pop3.quit()


if __name__ == "__main__":
    main()
    