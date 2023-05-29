"""
Zadanie 3
"""

import random
import socket

HOST = "127.0.0.1"  # Adres serwera
PORT = 12345  # Port serwera


def handle_client_connection(client_socket):
    # Losowanie liczby
    generated_number = random.randint(1, 100)

    while True:
        # Odbieranie wiadomości od klienta
        message = client_socket.recv(1024).decode("utf-8")

        try:
            guess = int(message)
        except ValueError:
            # Jeśli klient przesłał coś innego niż liczba, to wysłanie błędu
            response = "Błąd: Wprowadź liczbę."
        else:
            if guess < generated_number:
                response = "Liczba jest większa."
            elif guess > generated_number:
                response = "Liczba jest mniejsza."
            else:
                response = "Brawo! Odgadłeś liczbę."
                break

        # Wysłanie odpowiedzi do klienta
        client_socket.send(response.encode("utf-8"))

    # Zamknięcie połączenie z klientem
    client_socket.close()


def run_server():
    # Utworzenie gniazda serwera
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Serwer nasłuchuje na porcie {PORT}...")

    while True:
        # Akceptacja połączenia od klienta
        client_socket, address = server_socket.accept()
        print(f"Połączono z klientem: {address[0]}:{address[1]}")

        # Obsłużenie połączenia klienta w nowym wątku
        client_thread = threading.Thread(
            target=handle_client_connection, args=(client_socket,))
        client_thread.start()


run_server()
