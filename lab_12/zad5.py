import socket
import ssl


# Generowanie samodzielnie podpisanego certyfikatu
# Wymaga zainstalowanej biblioteki OpenSSL
def generate_self_signed_certificate():
    from OpenSSL import crypto, SSL

    # Generowanie klucza prywatnego
    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, 2048)

    # Tworzenie certyfikatu
    cert = crypto.X509()
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)  # Ważny przez 10 lat
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(pkey)
    cert.sign(pkey, "sha256")

    # Zapis certyfikatu i klucza prywatnego do plików
    with open("server.crt", "wb") as crt_file:
        crt_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    with open("server.key", "wb") as key_file:
        key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey))


def main():
    # Generowanie samodzielnie podpisanego certyfikatu
    generate_self_signed_certificate()

    # Adres i port serwera
    server_address = ("127.0.0.1", 1234)

    # Inicjalizacja gniazda
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)

    # Wstępne ustawienia SSL
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')

    # Nasłuchiwanie na połączenia
    server_socket.listen(1)
    print("Serwer oczekuje na połączenie...")

    while True:
        # Akceptowanie połączenia
        client_socket, client_address = server_socket.accept()
        print(f"Połączenie nawiązane z {client_address}")

        # Utworzenie bezpiecznego połączenia SSL
        secure_socket = ssl_context.wrap_socket(
            client_socket, server_side=True)

        # Odbieranie i odsyłanie wiadomości
        while True:
            data = secure_socket.recv(1024)
            if not data:
                break
            secure_socket.sendall(data)

        # Zakończenie połączenia
        secure_socket.close()
        print(f"Połączenie z {client_address} zakończone.")


if __name__ == "__main__":
    main()
