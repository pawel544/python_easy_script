import requests

key= ""
city= input()
url="http://api.openweathermap.org/data/2.5/weather"

parms={ "q":city,
        "appid":key,
        "units":"metric",
        "lang":"pl"
}

ans = requests.get(url,parms)

data = ans.json()
opd = data.get("rain",{} ).get("1h",0.0)

if ans.status_code == 200:
    print(f"Pogoda w   {city.capitalize()}:\n"
          f"Temperatura: {data['main']['temp']}C\n"
          f"Warunki: {data['weather'][0]['description']}\n"
          f"wiatr: {data['wind']['speed']} m/s\n"
          f"Opady: {opd} mm (ostatnia godzina) ")

else:
    print("Błąd pobierania danych spróbuj ponownie")