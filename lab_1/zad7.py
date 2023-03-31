"""
Zadanie 7
"""

import socket
import sys


if __name__ == "__main__":
    # pobieranie adresu serwera z argumentu linii poleceń
    server_address = sys.argv[1]

    # próba pobrania adresu IP dla podanej nazwy hostname
    try:
        ip = socket.gethostbyname(server_address)
    except socket.gaierror:
        print(f"Nie można pobrać adresu IP dla nazwy serwera {server_address}.")
        sys.exit()

    # iterowanie po wszystkich możliwych numerach portów (1-65535) i sprawdzanie, które są otwarte
    for port in range(1, 65536):
        # tworzenie gniazda
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # ustawienie timeout dla gniazda (aby uniknąć zawieszenia programu)
        sock.settimeout(0.5)

        # próba połączenia z serwerem na danym porcie
        result = sock.connect_ex((ip, port))

        # jeśli udało się nawiązać połączenie, port jest otwarty
        if result == 0:
            print(f"Port {port} jest otwarty.")

        # zamykanie gniazda
        sock.close()
