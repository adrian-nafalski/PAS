"""
Zadanie 8
"""

import socket
import sys


def fun():
    # pobieranie adresu serwera i numeru portu z argumentów linii poleceń
    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    buffer_size = 20  # maksymalna długość wiadomości

    # próba nawiązania połączenia z serwerem
    try:
        # tworzenie gniazda
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # próba połączenia z serwerem
        sock.connect((server_address, server_port))
        service_name = socket.getservbyport(server_port)
        print(f"Udało się nawiązać połączenie z serwerem {server_address} na porcie {server_port}. Usługa: {service_name}.")

        # wysyłanie i odbieranie wiadomości
        while True:
            message = input("Wprowadź wiadomość, którą chcesz wysłać: ")[:buffer_size]  # odczyt maksymalnie 20 znaków
            sock.sendall(message.encode())
            data = sock.recv(buffer_size)
            if not data:
                break
            print("Otrzymano z serwera:", data.decode())

    except (socket.timeout, socket.gaierror, ConnectionRefusedError):
        print(f"Nie udało się nawiązać połączenia z serwerem {server_address} na porcie {server_port}.")

    finally:
        # zamykanie gniazda
        sock.close()


if __name__ == "__main__":
    fun()
    