"""
Zadanie 7
"""

import ssl
import socket
import base64
import os


# Ustawienia serwera SMTP
smtp_server = "smtp.poczta.interia.pl"
port = 587


def main():
    # Dane logowania do serwera SMTP Interia.pl
    login = input("Podaj login: ")
    password = input("Podaj hasło: ")

    # Dane wiadomości
    from_address = input("Podaj adres nadawcy: ")
    to_address = input("Podaj adres odbiorcy: ")
    subject = input("Podaj temat wiadomości: ")
    message = input("Podaj treść wiadomości: ")

    # Dane załącznika
    file_path = input("Podaj ścieżkę do pliku: ")
    with open(file_path, "rb") as f:
        attachment = f.read()

    # Tworzenie gniazda sieciowego i połączenie z serwerem SMTP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((smtp_server, port))
    recv = client_socket.recv(1024).decode()
    print(recv)

    # Wysłanie komendy EHLO
    ehlo_command = 'EHLO example.com\r\n'
    client_socket.send(ehlo_command.encode())
    recv1 = client_socket.recv(1024).decode()
    print(recv1)

    # Wysłanie komendy STARTTLS
    tls_command = 'STARTTLS\r\n'
    client_socket.send(tls_command.encode())
    recv2 = client_socket.recv(1024).decode()
    print(recv2)

    # Ustawienie szyfrowania TLS
    ssl_context = ssl.create_default_context()
    client_socket = ssl_context.wrap_socket(
        client_socket, server_hostname=smtp_server)

    # Wysłanie komendy EHLO ponownie po ustanowieniu szyfrowania
    client_socket.send(ehlo_command.encode())
    recv3 = client_socket.recv(1024).decode()
    print(recv3)

    # Logowanie do serwera SMTP
    auth_command = 'AUTH LOGIN\r\n'
    client_socket.send(auth_command.encode())
    recv4 = client_socket.recv(1024).decode()
    print(recv4)

    # Wysłanie loginu i hasła
    login_command = base64.b64encode(login.encode()) + b'\r\n'
    client_socket.send(login_command)
    recv5 = client_socket.recv(1024).decode()
    print(recv5)

    password_command = base64.b64encode(password.encode()) + b'\r\n'
    client_socket.send(password_command)
    recv6 = client_socket.recv(1024).decode()
    print(recv6)

    # Wysłanie komendy MAIL FROM
    from_command = f'MAIL FROM: <{from_address}>\r\n'
    client_socket.send(from_command.encode())
    recv7 = client_socket.recv(1024).decode()
    print(recv7)

    # Wysłanie komendy RCPT TO
    to_command = f'RCPT TO: <{to_address}>\r\n'
    client_socket.send(to_command.encode())
    recv8 = client_socket.recv(1024).decode()
    print(recv8)

    # Wysłanie komendy DATA
    data_command = 'DATA\r\n'
    client_socket.send(data_command.encode())
    recv9 = client_socket.recv(1024).decode()
    print(recv9)

    # Wysłanie nagłówka wiadomości
    message_header = f'To: <{to_address}>\r\n' \
                    f'From: <{from_address}>\r\n' \
                    f'Subject: {subject}\r\n' \
                    f'MIME-Version: 1.0\r\n' \
                    f'Content-Type: multipart/mixed; boundary=boundary\r\n\r\n'
    client_socket.send(message_header.encode())

    # Wysłanie treści wiadomości
    message_body = f'--boundary\r\n' \
                f'Content-Type: text/plain; charset=utf-8\r\n\r\n' \
                f'{message}\r\n' \
                f'--boundary\r\n'

    # Wysłanie załącznika
    filename = os.path.basename(file_path)
    attachment_header = f'Content-Disposition: attachment; filename="{filename}"\r\n' \
                        f'Content-Type: application/octet-stream\r\n' \
                        f'Content-Transfer-Encoding: base64\r\n\r\n'

    encoded_attachment = base64.b64encode(attachment)
    attachment_body = encoded_attachment.decode() + '\r\n' + '--boundary--\r\n'

    client_socket.send(message_body.encode())
    client_socket.send(attachment_header.encode())
    client_socket.send(attachment_body.encode())

    # Wysłanie końca wiadomości
    end_command = '\r\n.\r\n'
    client_socket.send(end_command.encode())
    recv10 = client_socket.recv(1024).decode()
    print(recv10)

    # Wysłanie komendy QUIT i zamknięcie połączenia
    quit_command = 'QUIT\r\n'
    client_socket.send(quit_command.encode())
    recv11 = client_socket.recv(1024).decode()
    print(recv11)

    client_socket.close()


if __name__ == "__main__":
    main()
