"""
Zadanie 4
"""

import socket

SERVER_IP = "212.182.24.27"
SERVER_PORT = 2901

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input("Wprowadź wiadomość, którą chcesz wysłać: ")
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    data, address = client_socket.recvfrom(1024)
    print("Otrzymano z serwera:", data.decode())
    client_socket.close()


if __name__ == "__main__":
    udp_client()
