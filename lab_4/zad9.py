"""
Zadanie 9
"""

import socket

# adres i port serwera
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 5000

# wiadomość do wysłania w przypadku błędnego sformatowania
BAD_SYNTAX_MESSAGE = "BAD SYNTAX"

# funkcja do obsługi połączenia z klientem
def handle_client(client_socket, client_address):
    print(f"Nowe połączenie od {client_address}")

    while True:
        try:
            # odbieranie wiadomości od klienta
            data, _ = client_socket.recvfrom(1024)
            message = data.decode().strip()

            # weryfikacja poprawności formatu wiadomości
            parts = message.split(';')
            if len(parts) != 2 or parts[0] != "zad13" or not parts[1].isdigit():
                response = BAD_SYNTAX_MESSAGE
            else:
                # weryfikacja liczby z wiadomości
                number = int(parts[1])
                if number % 2 == 0:
                    response = "TAK"
                else:
                    response = "NIE"

            # wysłanie odpowiedzi do klienta
            client_socket.sendto(response.encode(), client_address)

        except socket.timeout:
            print(f"Połączenie z {client_address} zostało przerwane przez timeout")
            break

        except (socket.error, OSError):
            print(f"Wystąpił błąd podczas komunikacji z {client_address}")
            break

    client_socket.close()
    print(f"Połączenie z {client_address} zostało zakończone")


if __name__ == "__main__":
    # tworzenie gniazda UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
    server_socket.settimeout(5)

    print(f"Serwer nasłuchuje na adresie {SERVER_ADDRESS} i porcie {SERVER_PORT}")

    while True:
        try:
            # oczekiwanie na połączenie od klienta
            data, client_address = server_socket.recvfrom(1024)

            # obsługa połączenia w nowym wątku
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client_socket.sendto(data, client_address)
            handle_client(client_socket, client_address)

        except socket.timeout:
            print("Serwer czeka na połączenie...")

        except (socket.error, OSError):
            print("Wystąpił błąd podczas komunikacji z klientem")

        finally:
            server_socket.close()
