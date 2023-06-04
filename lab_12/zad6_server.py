import socket
import ssl

# Adres i port serwera
SERVER_ADDRESS = ("127.0.0.1", 12345)
CERT_FILE = "server.crt"
KEY_FILE = "server.key"


def main():
    # Tworzenie gniazda serwera
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(1)

    # Inicjalizacja kontekstu SSL
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    print("Serwer TCP działa...")

    while True:
        # Akceptowanie połączenia
        client_socket, client_address = server_socket.accept()
        print("Połączono z:", client_address)

        # Nawiązanie bezpiecznego połączenia SSL
        secure_socket = ssl_context.wrap_socket(
            client_socket, server_side=True)

        try:
            while True:
                # Odbieranie danych od klienta
                data = secure_socket.recv(1024)
                if not data:
                    break

                # Odsyłanie wiadomości do klienta
                secure_socket.sendall(data)

        except ssl.SSLError as e:
            print("Błąd SSL:", e)

        finally:
            # Zamykanie połączenia
            secure_socket.close()
            print("Połączenie z", client_address, "zamknięte")


if __name__ == "__main__":
    main()
