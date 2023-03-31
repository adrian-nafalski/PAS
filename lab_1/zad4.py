"""
Zadanie 4
"""

import socket
import sys


if __name__ == "__main__":
    # pobieranie adresu IP z argumentu linii poleceń
    ip = sys.argv[1]

    # próba pobrania nazwy hostname dla podanego adresu IP
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(f"Nazwa hostname dla adresu IP {ip} to {hostname}.")
    except socket.herror:
        print(f"Nie można pobrać nazwy hostname dla adresu IP {ip}.")
