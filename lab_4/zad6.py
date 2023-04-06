"""
Zadanie 6
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
            # Odbieranie nazwy hosta od klienta
            data, addr = s.recvfrom(1024)
            print(f"Otrzymano nazwę hosta {data.decode()} od {addr}")

            # Pobieranie adresu IP dla podanej nazwy hosta
            try:
                ip = socket.gethostbyname(data.decode())
                s.sendto(ip.encode(), addr)
                print(f"Wysłano adres IP {ip} do {addr}")
            except:
                s.sendto("Nie można odnaleźć adresu IP dla podanej nazwy hosta".encode(), addr)


if __name__ == "__main__":
    serv()
    