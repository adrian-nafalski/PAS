"""
Zadanie 5
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
            # Odbieranie adresu IP od klienta
            data, addr = s.recvfrom(1024)
            print(f"Otrzymano adres IP od {addr}: {data.decode()}")

            # Pobieranie nazwy hosta dla podanego adresu IP
            try:
                hostname = socket.gethostbyaddr(data.decode())[0]
                s.sendto(hostname.encode(), addr)
                print(f"Wysłano nazwę hosta {hostname} do {addr}")
            except:
                s.sendto("Nie można odnaleźć nazwy hosta dla podanego adresu IP".encode(), addr)


if __name__ == "__main__":
    serv()
