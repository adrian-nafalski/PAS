"""
Zadanie 3
"""

import requests

url = "http://212.182.24.27:8080/image.jpg"

def main():
    # Pobranie rozmiaru pliku (bez pobierania zawartości)
    response = requests.head(url)
    content_length = int(response.headers["Content-Length"])

    # Podzielenie rozmiaru na trzy części
    part_size = content_length // 3

    # Pobranie poszczególnych części obrazka
    parts = []
    for i in range(3):
        start_byte = i * part_size
        end_byte = start_byte + part_size - 1 if i < 2 else content_length - 1

        headers = {"Range": f"bytes={start_byte}-{end_byte}"}
        response = requests.get(url, headers=headers)
        parts.append(response.content)

    # Połączenie części w całość
    image_data = b''.join(parts)

    # Zapisanie obrazka do pliku
    with open("obrazek.jpg", "wb") as file:
        file.write(image_data)

if __name__ == "__main__":
    main()
    