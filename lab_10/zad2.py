"""
Zadanie 2
"""

import websocket


def on_open(ws):
    print("Połączenie nawiązane")
    message = "To jest moja wiadomość"
    ws.send(message)
    print(f"Wysłano wiadomość: {message}")


def on_message(ws, message):
    print(f"Otrzymano wiadomość: {message}")


def on_error(ws, error):
    print(f"Wystąpił błąd: {error}")


def on_close(ws):
    print("Połączenie z serwerem zamknięte")


def main():
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("ws://echo.websocket.org:80/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()


if __name__ == "__main__":
    main()
