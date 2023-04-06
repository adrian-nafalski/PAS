"""
Zadanie 7
"""

import socket

TCP_IP = "212.182.24.27"
TCP_PORT = 2900
BUFFER_SIZE = 20
MESSAGE = b'Witaj serwerze, z tej strony twoj klient!'


def tcp_client():
    # utworzenie gniazda (socket)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # nawiązanie połączenia
    s.connect((TCP_IP, TCP_PORT))
    # wysłanie wiadomości do serwera
    s.sendall(MESSAGE)
    # odbiór danych z serwera
    data = s.recv(BUFFER_SIZE)
    # wyświetlenie odebranej odpowiedzi
    print(f"Odpowiedź od serwera: {data.decode()}")
    # zamknięcie połączenia
    s.close()

if __name__ == "__main__":
    tcp_client()
