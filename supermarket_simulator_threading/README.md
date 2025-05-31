# Symulator Kolejek w Supermarkecie 🛒

Ten projekt to prosty symulator obsługi klientów w supermarkecie z 3 kasami. Klienci są generowani losowo, a następnie kierowani do najkrótszej z trzech kolejek. Każda kasa działa niezależnie i obsługuje swoich klientów w osobnych wątkach.

## 🔧 Jak to działa?

- Trzy kolejki (`Queue`) reprezentują kasy.
- Klienci są generowani z losowym imieniem i liczbą produktów.
- Klient trafia do najkrótszej kolejki.
- Czas obsługi klienta jest losowy lub zależny od liczby produktów.
- Symulacja trwa 60 sekund.

## 🧪 Wykorzystane biblioteki

- `threading` — do obsługi kas i generatora klientów jako osobne wątki
- `queue.Queue` — do bezpiecznego kolejkowania klientów
- `random` — do losowania imion, liczby produktów, czasu
- `time` — do symulacji czasu obsługi i oczekiwania

## ▶️ Uruchomienie

1. Upewnij się, że masz zainstalowanego Pythona 3.10 lub wyżej.
2. Uruchom skrypt w terminalu lub PyCharm:
```bash
python \supermarket_simulator
