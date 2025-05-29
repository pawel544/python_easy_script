import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")
df = pd.DataFrame(data)
dfi= df.fillna(value="NaN")
dfi['Przychód']=pd.to_numeric(dfi['Przychód'], errors='coerce')
print(dfi)

unikal_sum = dfi.groupby('Produkt')['Przychód'].sum()
unikal_summ = dfi.groupby(['Produkt','Miesiąc'])['Przychód'].sum().reset_index()
sre = unikal_summ.groupby('Produkt')['Przychód'].mean()
print(sre)
plt.figure(figsize=(4,5))
plt.bar(sre.index,sre.values)
plt.xlabel("Produkty")
plt.ylabel("Średnia miesięczna cena[PLN]")
plt.tight_layout()
plt.savefig('chart.jpg')
plt.show()
with open("raport.txt", 'w', encoding="utf-8") as e:
    e.write("📊 Raport sprzedaży\n\n")
    e.write("Sumaryczny przychód:\n")
    e.write(unikal_sum.to_string())
    e.write("\n\nŚredni miesięczny przychód:\n")
    e.write(sre.to_string())