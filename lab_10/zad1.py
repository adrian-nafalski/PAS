"""
Zadanie 1
"""

import websocket

# Ustalenie adresu serwera WebSocket
websocket_url = "ws://echo.websocket.org/"

def main():
    # Tworzenie klienta WebSocket
    ws = websocket.WebSocket()
    ws.connect(websocket_url)

    try:
        # Wysłanie wiadomości do serwera
        message = "Hello, server!"
        ws.send(message)
        print("Wysłano wiadomość:", message)

        # Odebranie odpowiedzi od serwera
        response = ws.recv()
        print("Odebrano odpowiedź:", response)

    finally:
        # Zamknięcie połączenia
        ws.close()

if __name__ == "__main__":
    main()
