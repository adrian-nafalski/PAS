"""
Zadanie 9
"""

import socket


if __name__ == "__main__":
    # adres serwera
    server_address = ('212.182.24.27', 2906)

    # tworzenie gniazda klienta
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # adres IP klienta
    client_address = socket.gethostbyname(socket.gethostname())

    # wysyłanie adresu IP do serwera
    client_socket.sendto(client_address.encode(), server_address)

    # odbieranie nazwy hostname od serwera
    data, _ = client_socket.recvfrom(1024)
    hostname = data.decode()

    print(f"Adres IP klienta: {client_address}")
    print(f"Nazwa hostname odpowiadająca adresowi IP {client_address}: {hostname}")

    # zamykanie gniazda klienta
    client_socket.close()
