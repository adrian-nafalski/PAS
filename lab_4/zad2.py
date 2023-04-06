"""
Zadanie 2
"""

import socket


def serv():
    HOST = "127.0.0.1"  # Adres serwera
    PORT = 12345       # Określony port TCP

    # Tworzenie gniazda
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Przypisanie adresu i portu do gniazda
        s.bind((HOST, PORT))
        # Nasłuchiwanie na porcie
        s.listen()
        print(f"Serwer działa pod adresem {HOST}:{PORT}")

        while True:
            # Akceptowanie połączenia
            conn, addr = s.accept()
            with conn:
                print(f"Połączenie z {addr} nawiązane")
                # Odbieranie danych od klienta
                data = conn.recv(1024)
                if not data:
                    break
                # Odsyłanie danych z powrotem do klienta
                conn.sendall(data)


if __name__ == "__main__":
    serv()
