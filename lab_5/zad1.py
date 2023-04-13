"""
Zadanie 1
"""

import socket


def client():
    # ustalenie adresu IP serwera i numeru portu
    HOST = "212.182.24.27"
    PORT = 2912

    # utworzenie gniazda sieciowego
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # połączenie z serwerem
    client_socket.connect((HOST, PORT))

    # pobranie liczby od użytkownika
    guess = input("Podaj liczbę: ")

    # wysłanie liczby do serwera
    client_socket.send(guess.encode())

    # odbiór odpowiedzi od serwera
    result = client_socket.recv(1024).decode()

    # wyświetlenie wyniku
    print(result)

    # zamknięcie gniazda sieciowego
    client_socket.close()


if __name__ == "__main__":
    client()
    