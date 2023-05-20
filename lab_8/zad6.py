"""
Zadanie 6
"""

import socket

# Adres serwera
PORT = 143
HOST = "127.0.0.1"

# Dostępne komendy IMAP
COMMANDS = ["LOGIN", "LIST", "FETCH", "LOGOUT"]

# Symulowane wiadomości e-mail
EMAILS = [
    {"id": 1, "subject": "Hello", "from": "sender@example.com"},
    {"id": 2, "subject": "Important Notice", "from": "notification@example.com"}
]

# Funkcja obsługująca komendy klienta
def handle_command(command):
    if command.startswith("LOGIN"):
        return "OK LOGIN completed"
    elif command.startswith("LIST"):
        response = "OK LIST completed\r\n"
        for email in EMAILS:
            response += f'{email["id"]} EXISTS\r\n'
        response += "LIST completed"
        return response
    elif command.startswith("FETCH"):
        email_id = int(command.split()[-1])
        for email in EMAILS:
            if email["id"] == email_id:
                response = f'OK FETCH completed\r\nSubject: {email["subject"]}\r\nFrom: {email["from"]}\r\n'
                return response
        return "ERROR Message not found"
    elif command.startswith("LOGOUT"):
        return "OK LOGOUT completed"
    else:
        return "ERROR Unknown command"

# Główna pętla serwera
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connected client: {client_address}")

            try:
                while True:
                    data = client_socket.recv(1024).decode("utf-8").strip()
                    if not data:
                        break

                    print(f"Received: {data}")
                    response = handle_command(data)
                    print(f"Response: {response}")

                    client_socket.sendall(response.encode("utf-8"))
            finally:
                client_socket.close()
                print("Client disconnected")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
