"""
Zadanie 2
"""

import random
import socket

# ustalenie adresu IP serwera i numeru portu
HOST = "127.0.0.1"
PORT = 2912


def serv():
    # utworzenie gniazda sieciowego
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # przypisanie adresu IP i numeru portu do gniazda sieciowego
    server_socket.bind((HOST, PORT))

    # nasłuchiwanie na połączenia przychodzące
    server_socket.listen()

    # losowanie liczby
    number = random.randint(1, 100)

    # obsługa połączenia
    while True:
        # oczekiwanie na połączenie
        client_socket, address = server_socket.accept()
        print(f"Połączono z {address}")

        # odbiór wiadomości od klienta
        data = client_socket.recv(1024).decode()

        # sprawdzenie, czy wiadomość klienta jest liczbą
        try:
            guess = int(data)
        except ValueError:
            client_socket.send("Błąd: oczekiwano liczby".encode())
            continue

        # porównanie liczby od klienta z wylosowaną liczbą
        if guess == number:
            client_socket.send("Brawo, odgadłeś liczbę!".encode())
            break
        elif guess < number:
            client_socket.send("Liczba jest za mała!".encode())
        else:
            client_socket.send("Liczba jest za duża!".encode())

        # zamknięcie połączenia z klientem
        client_socket.close()

    # zamknięcie gniazda sieciowego
    server_socket.close()


if __name__ == "__main__":
    serv()
