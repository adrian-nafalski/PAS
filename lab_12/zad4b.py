import socket
import ssl


def connect_with_server_verification():
    host = "212.182.24.27"
    port = 29443

    # Utworzenie gniazda klienta
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Nawiązanie zabezpieczonego połączeniea SSL/TLS z serwerem
        ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ssl_context.check_hostname = True
        ssl_context.verify_mode = ssl.CERT_REQUIRED
        ssl_socket = ssl_context.wrap_socket(client_socket)

        ssl_socket.connect((host, port))
        print("Połączono z serwerem.")

        while True:
            # Wczytanie tekstu od użytkownika
            message = input("Wpisz wiadomość: ")

            # Wysłanie wiadomości do serwera
            ssl_socket.send(message.encode())

            # Odebranie odpowiedzi od serwera
            response = ssl_socket.recv(1024).decode()
            print("Odpowiedź od serwera:", response)

    except ssl.SSLError as e:
        print("Błąd weryfikacji tożsamości serwera:", e)
    except ConnectionRefusedError:
        print("Nie można połączyć się z serwerem.")
    finally:
        # Zamknięcie gniazda SSL
        ssl_socket.close()


def main():
    # Wywołanie funkcji do nawiązania połączenia
    connect_with_server_verification()


if __name__ == "__main__":
    main()
