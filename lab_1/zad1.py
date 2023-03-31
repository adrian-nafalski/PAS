"""
Zadanie 1
"""

import shutil


if __name__ == "__main__":
    # nazwa pliku tekstowego do pobrania od użytkownika
    filename = input("Podaj nazwę pliku: ")

    # skopiowanie podanego pliku do "lab1zad1.txt"
    shutil.copy(filename, "lab1zad1.txt")
