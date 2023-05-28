"""
Zadanie 3
"""

import websocket


def on_message(ws, message):
    print("Otrzymano wiadomość:", message)


def on_error(ws, error):
    print("Wystąpił błąd:", error)


def on_close(ws):
    print("Połączenie zostało zamknięte")


def on_open(ws):
    print("Połączono z serwerem")
    message = "To jest moja wiadomość tekstowa o dowolnej długości!"
    ws.send(message)
    print("Wysłano wiadomość:", message)


def main():
    server_address = "ws://echo.websocket.org:80/"

    ws = websocket.WebSocketApp(server_address,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.on_open = on_open

    ws.run_forever()


if __name__ == "__main__":
    main()
