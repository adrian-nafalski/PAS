"""
Zadanie 6
"""

import socket
import sys


if __name__ == "__main__":
    # pobieranie adresu serwera i numeru portu z argumentów linii poleceń
    server_address = sys.argv[1]
    server_port = int(sys.argv[2])

    # próba nawiązania połączenia z serwerem
    try:
        # tworzenie gniazda
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # próba połączenia z serwerem
        sock.connect((server_address, server_port))
        print(f"Udało się nawiązać połączenie z serwerem {server_address} na porcie {server_port}.")
        
    except (socket.timeout, socket.gaierror, ConnectionRefusedError):
        print(f"Nie udało się nawiązać połączenia z serwerem {server_address} na porcie {server_port}.")
        
    finally:
        # zamykanie gniazda
        sock.close()
