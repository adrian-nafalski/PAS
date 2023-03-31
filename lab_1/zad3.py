"""
Zadanie 3
"""

import re

# funkcja do sprawdzania poprawności adresu IP
def is_valid_ip(ip):
    # wyrażenie regularne do sprawdzania poprawności adresu IP
    ip_regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(ip_regex, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    # pobieranie adresu IP od użytkownika
    ip = input("Podaj adres IP: ")

    # sprawdzanie poprawności adresu IP
    if is_valid_ip(ip):
        print("Adres IP jest poprawny.")
    else:
        print("Adres IP jest niepoprawny.")
