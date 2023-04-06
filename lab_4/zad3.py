"""
Zadanie 3
"""

import socket


def serv():
    HOST = "127.0.0.1"  # Adres serwera
    PORT = 12345       # Określony port UDP

    # Tworzenie gniazda
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Przypisanie adresu i portu do gniazda
        s.bind((HOST, PORT))
        print(f"Serwer działa pod adresem {HOST}:{PORT}")

        while True:
            # Odbieranie danych od klienta
            data, addr = s.recvfrom(1024)
            print(f"Otrzymano dane od {addr}: {data}")
            # Odsyłanie danych z powrotem do klienta
            s.sendto(data, addr)


if __name__ == "__main__":
    serv()
    