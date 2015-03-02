# usos-grades-checker
Projekt w założeniu miał być prostym sprawdzaczem ocen przez USOSAPI.
Z powodu niskiej przydatności (na oceny trzeba czekać - synchronizacja danych w USOSie jest raz na dobę) projekt został zawieszony po uzyskaniu pierwszej funkcjonalności.

Program napisany jest w kivy, więc teoretycznie powinien działać na platformach stacjonarnych i mobilnych. w praktyce różnie z tym bywa.


## Niezbędne biblioteki
* kivy
* oauth2

## Autoryzacja
Autoryzacja obywa się za pośrednictwem oauth. Klucze *Consumer Secret* oraz *Consumer Key* można wygenerować na stronie https://apps.usos.edu.pl/developers/
Do poprawnego działania programu koniecznie jest równiez wygenerowanie *Access Token* oraz *Access Secret*. Wartości należy zapisać w pliku secure_change.py i zmienić nazwę na secure.py.

## TODO
** Wrzucić narzędzie do generowania AT i AS

## Uruchaimianie
python main.py

## Budowanie na Androida
Heh...
