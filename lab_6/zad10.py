"""
Zadanie 10
"""

import socket

# Dane do logowania do serwera SMTP
smtp_server = "127.0.0.1"
smtp_port = 12345

# Obsługiwane komendy
supported_commands = ["EHLO", "MAIL FROM", "RCPT TO", "DATA", "QUIT"]


def main():
    # Inicjalizacja gniazda sieciowego
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((smtp_server, smtp_port))
    server_socket.listen()

    # Funkcja obsługująca komendy klienta
    def handle_command(command, client_socket):
        if command.startswith("EHLO"):
            response = "250 Hello\r\n"
        elif command.startswith("MAIL FROM"):
            response = "250 OK\r\n"
        elif command.startswith("RCPT TO"):
            response = "250 OK\r\n"
        elif command.startswith("DATA"):
            response = "354 Start mail input; end with <CRLF>.<CRLF>\r\n"
        elif command.startswith("QUIT"):
            response = "221 Bye\r\n"
        else:
            response = "500 Error: command not supported\r\n"
        client_socket.send(response.encode())


    # Główna pętla serwera
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Połączenie z {client_address} zostało nawiązane.")

        # Wysłanie wiadomości powitalnej
        welcome_message = "220 Welcome to SMTP server\r\n"
        client_socket.send(welcome_message.encode())

        # Obsługa komend klienta
        while True:
            command = client_socket.recv(1024).decode().strip()
            if not command:
                break
            print(f"Otrzymana komenda: {command}")
            handle_command(command, client_socket)

        client_socket.close()


if __name__ == "__main__":
    main()
    