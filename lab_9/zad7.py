"""
Zadanie 7
"""

import http.server
import socketserver

# Wybrane nagłówki
HEADERS = {"Content-type": "text/html; charset=utf-8"}

# Klasa obsługująca serwer
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Przesłonięcie metody do obsługi błędu 404
    def do_GET(self):
        if self.path == '/':
            # Wysyłanie strony głównej
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'<h1>Witaj na stronie glownej!</h1>')
        else:
            # Obsługa błędu 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'<h1>Blad 404 - Strona nie znaleziona</h1>')


# Konfiguracja i uruchomienie serwera
if __name__ == "__main__":
    # Adres i port serwera
    host = "127.0.0.1"
    port = 8000

    # Utworzenie serwera HTTP
    with socketserver.TCPServer((host, port), MyHTTPRequestHandler) as httpd:
        print("Serwer HTTP działa na adresie:", host)
        print("Port:", port)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
