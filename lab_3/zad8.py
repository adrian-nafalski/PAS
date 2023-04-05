"""
Zadanie 8
"""

import socket
import sys


def get_service_name(port):
    """
    Funkcja zwraca nazwę usługi uruchomionej na danym porcie
    """
    try:
        service_name = socket.getservbyport(port)
    except OSError:
        service_name = "unknown"
    return service_name


if __name__ == "__main__":
    # pobieranie adresu serwera z argumentu linii poleceń
    server_address = sys.argv[1]

    # próba pobrania adresu IP dla podanej nazwy hostname
    try:
        ip = socket.gethostbyname(server_address)
    except socket.gaierror:
        print(
            f"Nie można pobrać adresu IP dla nazwy serwera {server_address}.")
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
            service_name = get_service_name(port)
            print(f"Port {port} jest otwarty. Usługa: {service_name}")

        # jeśli nie udało się nawiązać połączenia, port jest zamknięty
        else:
            print(f"Port {port} jest zamknięty.")

        # zamykanie gniazda
        sock.close()
