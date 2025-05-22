import pandas as pd


data = pd.read_csv("developer_salaries.csv")

df = pd.DataFrame(data)

od= df.fillna(value='NaN')
medi= df["Salary"].median()
śred = df["Salary"].mean()



python_devs  = len(od[od["Language"] == "Python"])

top_5 = od.sort_values(["Salary"], ascending=False).head(5)



with open("raport.txt", "w", encoding="utf-8" ) as a:
    a.write(f"Średnie wynagrodzenie: {śred}\n")
    a.write(f"Mediana wynagrodzeń: {medi}\n")
    a.write(f"Liczba osób znająca Pythona: {python_devs}\n")
    a.write(f"Pięciu najlepiej zarabiających programistów \n")
    for i,row in top_5.iterrows():
        a.write(f"{row['Country']}     |     {row['Position']}     |     {row['Language']}     |     {row['Salary']}\n")

