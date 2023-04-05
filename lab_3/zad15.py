"""
Zadanie 15
"""

import socket


def fun():
    datagram = bytes.fromhex("45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b " \
                             "c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 " \
                             "80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 " \
                             "00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 " \
                             "72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e")
    
    source_ip, dest_ip, source_port, dest_port, data = datagram[12:16], datagram[16:20], datagram[20:22], datagram[22:24], datagram[52:]
    first_byte = bin(datagram[0])[2:].zfill(8)
    protocol_version = int(first_byte[:4], 2)
    protocol_type = 6
    
    print(f"Pierwszy bajt: {first_byte}")
    print(f"Źródłowe IP: {socket.inet_ntoa(source_ip)}")
    print(f"Docelowe IP: {socket.inet_ntoa(dest_ip)}")
    print(f"Port źródłowy: {int.from_bytes(source_port, byteorder='big')}")
    print(f"Port docelowy: {int.from_bytes(dest_port, byteorder='big')}")
    print(f"Dane: {data.decode()}")
    print(f"Typ protokołu: {protocol_type}")
    print(f"Wersja protokołu: {protocol_version}")
    
    odp1 = f"zad15odpA;ver;{protocol_version};srcip;{socket.inet_ntoa(source_ip)};dstip;{socket.inet_ntoa(dest_ip)};type;{protocol_type}"
    odp2 = f"zad15odpB;srcport;{int.from_bytes(source_port, byteorder='big')};dstport;{int.from_bytes(dest_port, byteorder='big')};data;{data.decode()}"
        
    print(odp1)
    print(odp2)
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.settimeout(1)
            sock.sendto(odp1.encode("utf-8"), ("212.182.24.27", 2911))
            result, _ = sock.recvfrom(1024)
            print(result.decode())
            sock.sendto(odp2.encode("utf-8"), ("212.182.24.27", 2911))
            result, _ = sock.recvfrom(1024)
            print(result.decode())
            print("Sukces!")
        except socket.timeout:
            print("Coś poszło nie tak")


if __name__ == "__main__":
    fun()
