"""
Zadanie 10
"""

import socket


if __name__ == "__main__":
    # adres serwera
    server_address = ('212.182.24.27', 2907)

    # tworzenie gniazda klienta
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # nazwa hosta klienta
    hostname = socket.gethostname()

    # wysyłanie nazwy hosta do serwera
    client_socket.sendto(hostname.encode(), server_address)

    # odbieranie adresu IP od serwera
    data, _ = client_socket.recvfrom(1024)
    ip_address = data.decode()

    print(f"Nazwa hosta klienta: {hostname}")
    print(f"Adres IP odpowiadający nazwie hosta {hostname}: {ip_address}")

    # zamykanie gniazda klienta
    client_socket.close()
