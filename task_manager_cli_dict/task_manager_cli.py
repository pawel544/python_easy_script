import json
tasks={0:{}}
try:
    with open("tasks.json", "r", encoding="utf-8") as a:
        tasks = json.load(a)
        tasks={int(x):v for x,v in tasks.items()}

except FileNotFoundError:
    print("Plik nie istnieje")

def add_task(task_text,priority,tasks):

    new_key = max(tasks)+1
    tasks[new_key]={"text":task_text,"priority":priority}
    print ("Zadanie dodano")

def show_all_tasks(tasks):
    try:
        for key, values in tasks.items():
            if key==0 :
                continue

            print(f"Nr{key}\n"
                  f" {values['text']} | {values['priority']} ")
    except KeyError:
        print("klucz nie znaleziony")
def delete_task(task_id_to_delete):
    try:
        del tasks[task_id_to_delete]
        print("usuwanie zakończone")
    except KeyError:
        print ("klucz nie istnieje")
def show_task(task_id_to_show):
    for key, values in tasks.items():

        if key==task_id_to_show:
            print (f"Nr {key}\n"
                   f"{values['text']} | {values['priority']}")


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
            break
    elif choice == "1":
        task_text = input("Podaj zadanie: ")
        priority = input("Ustal priorytet: ")
        add_task(task_text,priority,tasks)
    elif choice == "2":
        show_all_tasks(tasks)
    elif choice == "3":
        task_id_to_delete = int(input("Podaj numer zadania do usunięcia: "))
        delete_task(task_id_to_delete)
    elif choice == "4":
        task_id_to_show = str(input("Podaj Numer zadania do wyświetlenia"))
        show_task(task_id_to_show)