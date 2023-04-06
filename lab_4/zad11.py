"""
Zadanie 11
"""

import socket

HOST = "127.0.0.1"  # adres serwera
PORT = 5000  # port serwera UDP


def parse_message(msg):
    """Funkcja parsująca wiadomość od klienta"""
    try:
        parts = msg.decode().split(';')
        if len(parts) != 7:
            raise ValueError("Nieprawidłowy format wiadomości")
        elif parts[0] != 'zad15':
            raise ValueError("Nieprawidłowy identyfikator zadania")
        elif parts[1] != 'ver':
            raise ValueError("Nieprawidłowy typ pola")
        elif parts[3] != 'srcip':
            raise ValueError("Nieprawidłowy typ pola")
        elif parts[5] != 'type':
            raise ValueError("Nieprawidłowy typ pola")
        else:
            protocol_version = int(parts[2])
            source_ip = parts[4]
            protocol_type = int(parts[6])
            return (protocol_version, source_ip, protocol_type)
    except Exception as e:
        print(f"Błąd parsowania wiadomości: {e}")
        return None


def process_message(msg, addr, sock):
    """Funkcja przetwarzająca wiadomość od klienta"""
    parsed_msg = parse_message(msg)
    if parsed_msg is None:
        # błędny format wiadomości
        response = 'BAD SYNTAX'.encode()
    else:
        # poprawna wiadomość
        protocol_version, source_ip, protocol_type = parsed_msg
        if protocol_type == 6:
            # protokół TCP
            response = 'TAK'.encode()
        else:
            # inny protokół
            response = 'NIE'.encode()
    sock.sendto(response, addr)


def main():
    """Funkcja główna programu"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        print(f"Słucham na porcie {PORT}")
        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Otrzymano wiadomość od {addr}")
            process_message(data, addr, sock)


if __name__ == "__main__":
    main()
