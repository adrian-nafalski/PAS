"""
Zadanie 4 - client TCP
"""

import socket
import time


def client():
    # Tworzenie gniazda TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Ustawianie portu serwera i adresu IP
    server_port = 12345
    server_address = ("localhost", server_port)

    # Łączenie z serwerem
    client_socket.connect(server_address)

    # Wysyłanie danych do serwera
    data = b'Hello, world!'
    start_time = time.time()
    client_socket.sendall(data)

    # Odbieranie danych od serwera
    response = client_socket.recv(1024)

    end_time = time.time()

    print(f"Odebrano: {response.decode()}")
    print(f"Czas przesyłu (TCP): {end_time - start_time}")

    # Zamykanie połączenia
    client_socket.close()


if __name__ == "__main__":
    client()
    