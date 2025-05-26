import requests
from datetime import date, datetime





def nasa_raport(user_date,save_to_file):

    url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    try:
        if user_date.strip():
            valid_date = datetime.strptime(user_date, "%Y-%m-%d").date().isoformat()
            pram = {'date': valid_date }

        else:
            valid_date  = date.today().isoformat()

            pram = {'date': valid_date }
    except ValueError as e:
        print("Błędna data spróbó ponownie")
        return
    try:
        answer= requests.get(url,pram).json()


        raport = (f'🗓️ Data: {answer["date"]}\n'
                f'🖼️ Tytuł: {answer["title"]}\n'
                f'📝 Opis: {answer["explanation"]}\n'
                f'🔗 Link do zdjęcia: {answer.get("hdurl", answer.get("url", "Brak linku"))}')
        print(raport)
        if save_to_file:
            with open("raport.txt", "w", encoding="utf-8") as a:
                a.write(raport)
                print("📄 Raport zapisany do pliku `raport.txt`")
    except requests.RequestException as e:
        print("❌ Błąd połączenia 400")
while True:
    user_date = input("Podaj date w formacie RRRR-MM-DD \n"
                      "Albo wpisz exit by zakończyć: ")
    if user_date == "exit":break
    save= input("Chcesz wygenerować raport t/n").lower()

    save_raport = save == 't'
    nasa_raport(user_date,save_to_file = save_raport)