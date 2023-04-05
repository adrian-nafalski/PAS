"""
Zadanie 11
"""

import socket


def func():
    # adres serwera
    server_address = ('212.182.24.27', 2908)

    # tworzenie gniazda klienta
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # łączenie z serwerem
    client_socket.connect(server_address)

    # pobieranie wiadomości od użytkownika
    message = input("Podaj wiadomość do wysłania (maksymalnie 20 znaków): ")

    # uzupełnienie wiadomości spacjami, jeśli jest za krótka
    if len(message) < 20:
        message += " " * (20 - len(message))

    # przycięcie wiadomości do 20 znaków, jeśli jest za długa
    if len(message) > 20:
        message = message[:20]

    # wysyłanie wiadomości do serwera
    client_socket.sendall(message.encode())

    # odbieranie odpowiedzi od serwera
    data = client_socket.recv(20)

    # wypisywanie odpowiedzi na ekranie
    print(f"Otrzymana wiadomość: {data.decode()}")

    # zamykanie gniazda klienta
    client_socket.close()


if __name__ == "__main__":
    func()
