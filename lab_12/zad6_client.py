import socket
import ssl

# Adres i port serwera
SERVER_ADDRESS = ("127.0.0.1", 12345)
CERT_FILE = "client.crt"
KEY_FILE = "client.key"


def main():
    # Tworzenie gniazda klienta
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Inicjalizacja kontekstu SSL
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    # Nawiązanie bezpiecznego połączenia SSL
    secure_socket = ssl_context.wrap_socket(client_socket)

    # Połączenie z serwerem
    secure_socket.connect(SERVER_ADDRESS)
    print("Połączono z serwerem", SERVER_ADDRESS)

    try:
        while True:
            # Wczytywanie wiadomości od użytkownika
            message = input("Wiadomość do serwera: ")

            # Wysyłanie wiadomości do serwera
            secure_socket.sendall(message.encode())

            # Odbieranie odpowiedzi od serwera
            data = secure_socket.recv(1024)
            print("Odpowiedź serwera:", data.decode())

    except ssl.SSLError as e:
        print("Błąd SSL:", e)

    finally:
        # Zamykanie połączenia
        secure_socket.close()
        print("Połączenie z serwerem zamknięte")


if __name__ == "__main__":
    main()
