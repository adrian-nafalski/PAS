"""
Zadanie 4
"""

import requests

# Adres serwera
url = "http://httpbin.org/post"


def main():
    # Pobranie danych od użytkownika
    name = input("Podaj imię: ")
    age = input("Podaj wiek: ")

    # Utworzenie danych do wysłania
    data = {
        "name": name,
        "age": age
    }

    # Wysłanie żądania POST na serwer
    response = requests.post(url, data=data)

    # Wyświetlenie odpowiedzi serwera
    print(response.text)

if __name__ == "__main__":
    main()
