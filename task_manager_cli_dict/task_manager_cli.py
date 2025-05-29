import json
tasks={0:{}}
try:
    with open("tasks.json", "r", encoding="utf-8") as a:
        tasks = json.load(a)
        tasks={int(x):v for x,v in tasks.items()}

except FileNotFoundError:
    print("Plik nie istnieje")

def add_task(task_text,priority,tasks):
    if priority  in ["wysoki","średni","niski" ]:
        new_key = max(tasks)+1
        tasks[new_key]={"text":task_text,"priority":priority}
        print ("Zadanie dodano")
    else:
        print("Dozwolone priorytety: wysoki, średni, niski ")

def show_all_tasks(tasks):
    try:
        for key, values in tasks.items():
            if key==0 :
                continue

            print(f"🆔Nr{key}\n"
                  f"✏️{values['text']} |⏱️Priorytet: {values['priority']} ")
    except KeyError:
        print("❌klucz nie znaleziony")
def delete_task(task_id_to_delete):
    try:
        del tasks[task_id_to_delete]
        print("🗑usuwanie zakończone")
    except KeyError:
        print ("❌klucz nie istnieje")
def show_task(task_id_to_show):
    for key, values in tasks.items():

        if key==task_id_to_show:
            print (f"🆔Nr: {key}\n"
                   f"✏️{values['text']} |⏱️Priorytet: {values['priority']}")
    else:
        print(f"❌Błędny numer zadania")


while True:

    choice= input(
        "\n📋 MENU:\n"
        "1- Dodaj zadanie\n"
        "2- Wyświetl wszystkie zadania\n"
        "3- Usuń zadanie\n"
        "4- Pokaż -jedno zadanie\n"
        "Exit- wyjście\n"
        "👉 Wybierz opcję:")
    if choice=="exit":
        with open("tasks.json", "w", encoding="utf-8") as r:
            json.dump(tasks, r, indent=4)
            print("💾Zapisywanie zakończone do zobaczenia")
            break
    elif choice == "1":
        try:
            task_text = input("👉Podaj zadanie: ")
            priority = input("👉Ustal priorytet(wysoki,średni,niski): ").strip().lower()
            add_task(task_text,priority,tasks)
        except Exception as e:
            print(f'❌Błedny priorytet spróbuj ponownie')
    elif choice == "2":
        try:
            show_all_tasks(tasks)
        except Exception as e:
            print(f"❌Nieoczekiwany błąd spróbuj ponownie {e}")
    elif choice == "3":
        try:
            task_id_to_delete = int(input("👉Podaj numer zadania do usunięcia: "))
            delete_task(task_id_to_delete)
        except Exception as e:
            print("❌Błędny numer zadania spróbuj ponownie")
    elif choice == "4":
        try:
            task_id_to_show = int(input("👉Podaj Numer zadania do wyświetlenia"))
            show_task(task_id_to_show)
        except Exception as e:
            print("❌Błędny numer zadania spróbuj ponownie")