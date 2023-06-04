import socket


def connect_without_server_verification():
    host = "212.182.24.27"
    port = 29443

    # Utworzenie gniazda klienta
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Nawiązanie połączenia z serwerem
        client_socket.connect((host, port))
        print("Połączono z serwerem.")

        while True:
            # Wczytanie tekstu od użytkownika
            message = input("Wpisz wiadomość: ")

            # Wysłanie wiadomości do serwera
            client_socket.send(message.encode())

            # Odebranie odpowiedzi od serwera
            response = client_socket.recv(1024).decode()
            print("Odpowiedź od serwera:", response)

    except ConnectionRefusedError:
        print("Nie można połączyć się z serwerem.")
    finally:
        # Zamknięcie gniazda klienta
        client_socket.close()


def main():
    # Wywołanie funkcji do nawiązania połączenia
    connect_without_server_verification()


if __name__ == "__main__":
    main()
