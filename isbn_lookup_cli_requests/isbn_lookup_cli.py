import requests

number_isbn= input("Podaj numer ISBP: ")

def book(number_isbn):
       url=f"https://www.googleapis.com/books/v1/volumes?q=isbn:{number_isbn}"
       if number_isbn.isdigit() and len(number_isbn) == 13:
              answer = requests.get(url).json()

#9780140328721
              data = f"📚 Tytuł: {answer['items'][0]['volumeInfo']['title']}\n" \
                     f"✍️ Autor: {answer['items'][0]['volumeInfo']['authors']}\n"\
                     f"🏢 Wydawnictwo: {answer['items'][0]['volumeInfo']['publisher']}\n"\
                     f"📅 Rok: {answer['items'][0]['volumeInfo']['publishedDate']}\n" \
                     f"📖 Liczba stron: {answer['items'][0]['volumeInfo']['pageCount']}\n" \

              return (data)
       else:
              return ("Błędny numer ISBN")

print(book(number_isbn))