# Pizzeria
Projekt systemu obsługi pizzerii

Aby uruchomić aplikację, zainstaluj wymagane biblioteki
'pip install -r requirements.txt'

Zaimportuj plik dbo.sql do bazy danych:

1. Otwórz terminal w katalogu, w którym masz pliki pizzeria.db i dbo.sql.
2. Wykonaj polecenie:
   'sqlite3 pizzeria.db < dbo.sql'
3. Jeśli wszystko pójdzie dobrze, baza danych pizzeria.db powinna zawierać tabele menu oraz zamowienia, a także dane zdefiniowane w pliku dbo.sql.

Po zaimportowaniu danych sprawdź, czy tabele zostały poprawnie utworzone:

1. Otwórz bazę danych:
   'sqlite3 pizzeria.db'
2. Sprawdź, jakie tabele istnieją:
   '.tables'
   Powinna pojawić się tabela menu oraz zamowienia.

Uruchom serwer:
'uvicorn main:app --reload'

Swagger będzie dostępny pod adresem http://127.0.0.1:8000/docs.
