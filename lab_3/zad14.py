"""
Zadanie 14
"""

import socket


def fun():
    datagram = bytes.fromhex("0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 " \
                             "00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee " \
                             "00 1a 4c ee 68 65 6c 6c 6f 20 3a 29")
    
    source_port, dest_port, data = datagram[:2], datagram[2:4], datagram[32:]

    print(f"Port źródłowy: {int.from_bytes(source_port, byteorder='big')}")
    print(f"Port docelowy: {int.from_bytes(dest_port, byteorder='big')}")
    print(f"Dane: {data.decode()}")

    odp = f"zad13odp;src;{int.from_bytes(source_port, byteorder='big')};dst;{int.from_bytes(dest_port, byteorder='big')};data;{data.decode()}"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.settimeout(1)
            sock.sendto(odp.encode("utf-8"), ("212.182.24.27", 2909))
            result, _ = sock.recvfrom(1024)
            print(result.decode())
            print("Sukces!")
        except socket.timeout:
            print("Coś poszło nie tak")

if __name__ == "__main__":
    fun()
