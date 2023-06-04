import smtplib
import ssl

# Dane serwera SMTP
smtp_port = 465
smtp_server = "smtp.gmail.com"
smtp_username = "pasinf2017@gmail.com"
smtp_password = "P4SInf2017"

# Dane wiadomości
from_email = input("Podaj adres nadawcy: ")
to_email = input("Podaj adres odbiorcy: ")
subject = input("Podaj temat wiadomości: ")
message = input("Podaj treść wiadomości: ")


def main():
    # Tworzenie wiadomości e-mail
    email_message = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{message}"

    try:
        # Tworzenie kontekstu SSL z weryfikacją certyfikatu
        context = ssl.create_default_context()

        # Nawiązanie połączenia z serwerem SMTP
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)

        # Logowanie do serwera SMTP
        smtp.login(smtp_username, smtp_password)

        # Wysłanie wiadomości e-mail
        smtp.sendmail(from_email, to_email, email_message)

        print("Wiadomość została wysłana pomyślnie.")

    except Exception as e:
        print("Wystąpił błąd podczas wysyłania wiadomości:", str(e))

    finally:
        # Zamknięcie połączenia z serwerem SMTP
        smtp.quit()


if __name__ == "__main__":
    main()
