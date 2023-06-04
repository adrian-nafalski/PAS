import requests

url = "https://httpbin.org/html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"
}


def main():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content = response.content

        with open("strona.html", "wb") as file:
            file.write(content)
            print("Strona została zapisana jako plik strona.html")
    else:
        print("Błąd podczas pobierania strony:", response.status_code)


if __name__ == "__main__":
    main()
