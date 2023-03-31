"""
Zadanie 5
"""

import socket
import sys


if __name__ == "__main__":
    # pobieranie nazwy hostname z argumentu linii poleceń
    hostname = sys.argv[1]

    # próba pobrania adresu IP dla podanej nazwy hostname
    try:
        ip = socket.gethostbyname(hostname)
        print(f"Adres IP dla nazwy hostname {hostname} to {ip}.")
    except socket.gaierror:
        print(f"Nie można pobrać adresu IP dla nazwy hostname {hostname}.")
