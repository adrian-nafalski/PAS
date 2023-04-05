"""
Zadanie 1
"""

import socket
import struct
import time  

NTP_SERVER = "ntp.task.gda.pl"  # adres serwera
NTP_PORT = 13  # nr portu
TIME1970 = 2208988800  # 1970-01-01 00:00:00


def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data, (NTP_SERVER, NTP_PORT))
    data, address = client.recvfrom(1024)  # bez address program nie zadziała
    if len(data) >= 48:
        t = struct.unpack("!12I", data)[10]
        t -= TIME1970
        print(f"Aktualna data i czas: {time.ctime(t)}")
    else:
        print("Nieprawidłowa odpowiedź SNTP ... ")


if __name__ == "__main__":
    sntp_client()
