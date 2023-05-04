"""
Zadanie 11
"""

import poplib
import email
import base64


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

    # Pobranie wiadomości z załącznikiem
    for i in range(num_messages):
        response = pop3.retr(i+1)
        message_lines = response[1]
        message_content = b'\n'.join(message_lines).decode("utf-8")
        message = email.message_from_string(message_content)

        # Sprawdzenie, czy wiadomość zawiera załącznik
        if message.get_content_maintype() == "multipart":
            for part in message.walk():
                if part.get_content_maintype() == "multipart" or part.get("Content-Disposition") is None:
                    continue
                # Pobranie nazwy załącznika i jego zawartości
                filename = part.get_filename()
                content = part.get_payload(decode=True)
                if filename is not None and content is not None:
                    # Odkodowanie zawartości załącznika z kodowania Base64
                    decoded_content = base64.b64decode(content)

                    # Zapisanie załącznika na dysku z nazwą odpowiadającą nazwie załącznika w mailu
                    with open(filename, "wb") as f:
                        f.write(decoded_content)

    # Zamknięcie połączenia z serwerem POP3
    pop3.quit()


if __name__ == "__main__":
    main()
