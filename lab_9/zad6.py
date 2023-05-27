"""
Zadanie 6
"""

import requests

url = "http://212.182.24.27:8080/image.jpg"
etag_file = "etag.txt"


def main():
    # Sprawdzenie, czy istnieje plik z zapisanym ETag
    try:
        with open(etag_file, "r") as file:
            saved_etag = file.read().strip()
    except FileNotFoundError:
        saved_etag = None

    # Wysłanie żądania HEAD, aby otrzymać ETag
    response = requests.head(url)
    new_etag = response.headers.get("ETag")

    # Porównanie ETag zapisanego z aktualnym
    if new_etag == saved_etag:
        print("Obrazek nie zmienił się. Nie trzeba go pobierać.")
        return

    # Pobranie rozmiaru pliku (bez pobierania zawartości)
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

    # Zapisanie nowego ETag do pliku
    with open(etag_file, "w") as file:
        file.write(new_etag)

    print("Obrazek został pobrany.")


if __name__ == "__main__":
    main()
