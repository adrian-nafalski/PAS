"""
Zadanie 4
"""

import asyncio
import websockets


async def handle_message(websocket, path):
    async for message in websocket:
        print(f"Odebrano wiadomość: {message}")
        response = f"Odpowiedź na: {message}"
        await websocket.send(response)
        print(f"Wysłano odpowiedź: {response}")


def main():
    start_server = websockets.serve(handle_message, "127.0.0.1", 8000)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
