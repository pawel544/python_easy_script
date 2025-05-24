import requests

kurs = input("podaj walute obcą: ")
wal_doc = input("podaj walute docelową: ")
kwota = input("Podaj kwote")
walut_list= [wal_doc, kwota]
nbp = url = f"http://api.nbp.pl/api/exchangerates/rates/a/{kurs}/last/{1}/?format=json"
if wal_doc =="PLN":
    nbp = url = f"http://api.nbp.pl/api/exchangerates/rates/a/{kurs}/last/{1}/?format=json"
    answer = requests.get(nbp).json()

    new_wal = (answer['rates'][0]['mid'])
    result = float( kwota)* new_wal
    print(f"💱 Dokonałeś przewalutowania: {kwota} {wal_doc.upper()} co pozwoliło Ci uzyskać {round(result, 2)} {kurs.upper()} ")
else:
    nbp_1 = url = f"http://api.nbp.pl/api/exchangerates/rates/a/{kurs}/last/{1}/?format=json"
    nbp_2 = url = f"http://api.nbp.pl/api/exchangerates/rates/a/{wal_doc}/last/{1}/?format=json"
    answer_1 = requests.get(nbp_1).json()
    answer_2 = requests.get(nbp_2).json()

    new_wal_1 = (answer_1['rates'][0]['mid'])
    new_wal_2 = (answer_2['rates'][0]['mid'])
    result = float(kwota) * (new_wal_1 / new_wal_2)
    print(f"💱 Dokonałeś przewalutowania: {kwota} {wal_doc.upper()} co pozwoliło Ci uzyskać {round(result, 2)} {kurs.upper()} ")




