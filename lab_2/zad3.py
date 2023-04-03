"""
Zadanie 3
"""

import socket

SERVER_IP = "212.182.24.27"
SERVER_PORT = 2900

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Poprawnie połączono z serwerem!")
    while True:
        message = input("Wprowadź wiadomość, którą chcesz wysłać: ")
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        if not data:
            break
        print("Otrzymano z serwera:", data.decode())
    client_socket.close()


if __name__ == "__main__":
    tcp_client()
