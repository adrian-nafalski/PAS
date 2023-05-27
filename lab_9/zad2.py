"""
Zadanie 2
"""

import requests

url = "http://httpbin.org/image/png"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
}

def main():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open("image.png", "wb") as file:
            file.write(response.content)
            print("Obrazek został pobrany i zapisany jako image.png.")
    else:
        print("Błąd podczas pobierania obrazka:", response.status_code)

if __name__ == "__main__":
    main()
    