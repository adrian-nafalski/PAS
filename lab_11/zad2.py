"""
Zadanie 2
"""

import socket
from datetime import datetime


def run_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Serwer echa uruchomiony na adresie {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Połączono z klientem {client_address[0]}:{client_address[1]}")

        # Zapisanie informacji do pliku
        with open("log.txt", "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(
                f"{timestamp}: Nowe połączenie od {client_address[0]}:{client_address[1]}\n")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall(data)

        client_socket.close()
        print(
            f"Połączenie z klientem {client_address[0]}:{client_address[1]} zakończone")

        # Zapisanie informacji do pliku
        with open("log.txt", "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(
                f"{timestamp}: Zakończone połączenie z {client_address[0]}:{client_address[1]}\n")

    server_socket.close()


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    run_server(host, port)
