"""
Zadanie 1
"""

import requests

url = "http://httpbin.org/html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Safari/9537.74.9",
    "Accept": "text/html"
}

def main():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open("page.html", "w") as file:
            file.write(response.text)
            print("Strona została pobrana i zapisana jako page.html.")
    else:
        print("Błąd podczas pobierania strony:", response.status_code)

if __name__ == "__main__":
    main()
