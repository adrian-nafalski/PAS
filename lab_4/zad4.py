"""
Zadanie 4
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

            # Parsowanie danych wejściowych
            try:
                num1, op, num2 = data.decode().split()
                num1, num2 = int(num1), int(num2)
            except:
                s.sendto("Niepoprawne dane wejściowe".encode(), addr)
                continue

            # Wykonanie operacji
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            else:
                s.sendto("Niepoprawny operator".encode(), addr)
                continue

            # Odsyłanie wyniku do klienta
            s.sendto(str(result).encode(), addr)


if __name__ == "__main__":
    serv()
