"""
Zadanie 13
"""

import socket


def fun():
    datagram = bytes.fromhex("ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 " \
                             "6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f " \
                             "6e 20 69 73 20 66 75 6e")
    
    source_port, dest_port, length, checksum, data = datagram[:2], datagram[2:4], datagram[4:6], datagram[6:8], datagram[8:]

    print(f"Port źródłowy: {int.from_bytes(source_port, byteorder='big')}")
    print(f"Port docelowy: {int.from_bytes(dest_port, byteorder='big')}")
    print(f"Długość: {int.from_bytes(length, byteorder='big')}")
    print(f"Suma kontrolna: {int.from_bytes(checksum, byteorder='big')}")
    print(f"Dane: {data.decode()}")

    odp = f"zad14odp;src;{int.from_bytes(source_port, byteorder='big')};dst;{int.from_bytes(dest_port, byteorder='big')};data;{data.decode()}"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.settimeout(1)
            sock.sendto(odp.encode("utf-8"), ("212.182.24.236", 2910))
            result, _ = sock.recvfrom(1024)
            print(result.decode())
            print("Sukces!")
        except socket.timeout:
            print("Coś poszło nie tak")
                
                
if __name__ == "__main__":
    fun()
    