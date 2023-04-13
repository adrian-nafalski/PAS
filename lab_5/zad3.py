"""
Zadanie 3 - Port-knocking
"""

import socket


# adres IP serwera oraz numer portu, na którym działa ukryta usługa
SERVER_IP = "212.182.24.27"
SERVER_TCP_PORT = 2913

# porty UDP, które należy sprawdzić w celu odkrycia sekwencji otwierającej port TCP
UDP_PORTS = [1000, 2000, 3000, 4000, 5000]

# funkcja, która sprawdza, czy dany port UDP jest częścią sekwencji otwierającej port TCP
def check_port(port):
    # tworzymy gniazdo UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # wysyłamy wiadomość PING na dany port UDP
    udp_socket.sendto(b'PING', (SERVER_IP, port))
    # oczekujemy na odpowiedź PONG z serwera przez 5 sekund
    udp_socket.settimeout(5)
    try:
        response, address = udp_socket.recvfrom(1024)
        # jeśli otrzymaliśmy odpowiedź PONG, oznacza to, że dany port jest częścią sekwencji
        if response == b'PONG':
            return True
    except socket.timeout:
        pass
    # jeśli nie otrzymaliśmy odpowiedzi, lub była inna niż PONG, oznacza to, że dany port nie jest częścią sekwencji
    return False


# funkcja główna
def main():
    # szukamy sekwencji otwierającej port TCP
    sequence = []
    for port in UDP_PORTS:
        if check_port(port):
            sequence.append(port)
    # jeśli udało się znaleźć sekwencję, to łączymy się z ukrytą usługą przez port TCP 2913
    if sequence:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((SERVER_IP, SERVER_TCP_PORT))
        # wysyłamy wiadomość zapytania do ukrytej usługi
        tcp_socket.send(b'Congratulations! You found the hidden')
        # odbieramy odpowiedź
        response = tcp_socket.recv(1024)
        print(response.decode())
        # zamykamy gniazdo TCP
        tcp_socket.close()
    else:
        print("Nie udało się znaleźć sekwencji portów UDP.")


if __name__ == "__main__":
    main()
