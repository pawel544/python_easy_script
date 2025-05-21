from collections import Counter
#pl="C:\Users\pawel\PycharmProjects\analiza_tekstu\text.txt"





with open("text.txt", "r", encoding='utf-8') as plik:
    text= plik.read()
    print(text)
znaki= [",", ".", "?"]
wo=text
for zn in znaki:

    wo=wo.replace(zn ,"")

tex= text.split(".")
number_of_sentences= len([z for z in tex if z.strip() !=""])
words= wo.lower().split()
number_words = len(words)

average_length = round(len(wo.replace(" ","")) / number_words,2)

words_counter = Counter(words)
top_10 = words_counter.most_common(10)
raport= (f"liczba zdań: {number_of_sentences}\n"
         f"liczba słów: {number_words}\n"
         f"Średnia długość słowa: {average_length}\n"
         f"Top 10: \n")


for liczb, zdan in top_10:
    raport+= f"{liczb} {zdan}\n"
print(raport)




with open("raport.txt", "w", encoding="utf-8") as a:
    a.write(raport)