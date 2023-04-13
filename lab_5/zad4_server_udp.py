"""
Zadanie 4 - server UDP
"""

import socket


def serv():
    # Tworzenie gniazda UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Ustawianie portu serwera i adresu IP
    server_port = 12345
    server_address = ("localhost", server_port)

    # Bindowanie gniazda
    server_socket.bind(server_address)

    print(f"Serwer UDP nasłuchuje na porcie {server_port}")

    while True:
        # Odbieranie danych od klienta
        data, client_address = server_socket.recvfrom(1024)
        print(f"Odebrano {len(data)} bajtów od {client_address}")

        # Wysyłanie danych do klienta
        server_socket.sendto(data, client_address)


if __name__ == "__main__":
    serv()
    