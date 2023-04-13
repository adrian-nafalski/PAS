"""
Zadanie 4 - client UDP
"""

import socket
import time


def client():
    # Tworzenie gniazda UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Ustawianie portu serwera i adresu IP
    server_port = 12345
    server_address = ("localhost", server_port)

    # Wysyłanie danych do serwera
    data = b'Hello, world!'
    start_time = time.time()
    client_socket.sendto(data, server_address)

    # Odbieranie danych od serwera
    response, server_address = client_socket.recvfrom(1024)

    end_time = time.time()

    print(f"Odebrano: {response.decode()}")
    print(f"Czas przesyłu (UDP): {end_time}")


if __name__ == "__main__":
    client()
    