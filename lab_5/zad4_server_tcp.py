"""
Zadanie 4 - sever TCP
"""

import socket


def serv():
    # Tworzenie gniazda TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Ustawianie portu serwera i adresu IP
    server_port = 12345
    server_address = ("localhost", server_port)

    # Bindowanie gniazda
    server_socket.bind(server_address)

    # Nasłuchiwanie na połączenia przychodzące
    server_socket.listen()

    print(f"Serwer TCP nasłuchuje na porcie {server_port}")

    while True:
        # Akceptowanie połączenia przychodzącego
        client_socket, client_address = server_socket.accept()
        print(f"Połączenie od {client_address}")

        # Odbieranie danych od klienta
        data = client_socket.recv(1024)

        # Wysyłanie danych do klienta
        client_socket.sendall(data)

        # Zamykanie połączenia
        client_socket.close()


if __name__ == "__main__":
    serv()
    