"""
Zadanie 12
"""

import socket


# przykładowe dane o wiadomościach
messages = [
    {"uid": "1", "size": 500,
        "header": "From: sender1@example.com\nTo: recipient1@example.com\nSubject: Test message 1\n\n"},
    {"uid": "2", "size": 700,
        "header": "From: sender2@example.com\nTo: recipient2@example.com\nSubject: Test message 2\n\n"},
    {"uid": "3", "size": 900,
        "header": "From: sender3@example.com\nTo: recipient3@example.com\nSubject: Test message 3\n\n"}
]


def handle_client(conn):
    conn.send(b"+OK POP3 server ready\n")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        command = data.decode().strip()
        if command == "QUIT":
            conn.send(b"+OK Bye\n")
            break
        elif command == "USER":
            conn.send(b"+OK\n")
        elif command == "PASS":
            conn.send(b"+OK\n")
        elif command == "STAT":
            num_messages = len(messages)
            total_size = sum([m["size"] for m in messages])
            conn.send(f"+OK {num_messages} {total_size}\n".encode())
        elif command == "LIST":
            conn.send(b"+OK\n")
            for i, m in enumerate(messages):
                conn.send(f"{i+1} {m['size']}\n".encode())
            conn.send(b".\n")
        elif command.startswith("RETR"):
            uid = command.split()[1]
            message = next((m for m in messages if m["uid"] == uid), None)
            if message:
                conn.send(b"+OK\n")
                conn.send(message["header"].encode())
                # tu można dodać symulacje przesyłania treści wiadomości
                conn.send(b".\n")
            else:
                conn.send(b"-ERR No such message\n")
        else:
            conn.send(b"-ERR Command not supported\n")

    conn.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 110))
    server_socket.listen(1)

    print("POP3 server listening on port 110...")

    while True:
        conn, addr = server_socket.accept()
        print(f"New client connected: {addr}")
        handle_client(conn)


if __name__ == "__main__":
    start_server()
