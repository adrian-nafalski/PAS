"""
Zadanie 10
"""

import socket


def fun():
    # Adres IP i port, na którym nasłuchujemy
    HOST = "127.0.0.1"
    PORT = 5000

    # Tworzymy socket typu datagramowego (UDP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Przypisujemy adres i port do socketu
    server_socket.bind((HOST, PORT))

    while True:
        # Oczekujemy na przyjście danych
        data, address = server_socket.recvfrom(1024)

        try:
            # Dekodujemy dane jako string
            message = data.decode()

            # Sprawdzamy, czy wiadomość jest poprawnie sformatowana
            if not message.startswith("zad14;data;"):
                raise ValueError("BAD SYNTAX")

            # Wyciągamy z wiadomości treść
            message = message[len("zad14;data;"):]

            # Wysyłamy odpowiedź w zależności od treści wiadomości
            if message == "hello world :)":
                server_socket.sendto(b'TAK', address)
            else:
                server_socket.sendto(b'NIE', address)

        except Exception as e:
            # Jeśli wystąpił błąd, wysyłamy odpowiedź BAD SYNTAX
            server_socket.sendto(b'BAD SYNTAX', address)
            print(e)

        finally:
            # Zamykamy socket (nie osiągalne w tym kodzie, ponieważ pętla jest nieskończona)
            server_socket.close()


if __name__ == "__main__":
    fun()
    