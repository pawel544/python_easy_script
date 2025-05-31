import threading
from queue import Queue
import random
import time
from threading import Thread
kolejka_1 =Queue()
kolejka_2 = Queue()
kolejka_3 = Queue()
def client ():
    client={"name" : random.choice(["Nikodem", "Antoni", "Jan", "Aleksander", "Leon", \
            "Franciszek", "Ignacy", "Jakub", "Stanisław"]),
            "product": random.randint(1,25)}
    return client

def kas_1():
    while True:
        print("Nowy  Klient")
        costume = kolejka_1.get()
        print(f' [kasa 1] obsługuje {costume["name"]} który posiada {costume["product"]}')
        time.sleep( random.randint(3,7))
        print(f"kasa 1 zakończyła obsługe {costume['name']}")
def kas_2():
    while True:
        print("Nowy Klient")
        costume = kolejka_2.get()
        print(f' [kasa 2] obsługuje {costume["name"]} który posiada {costume["product"]}')
        time.sleep( random.randint(3,7))
        print(f"kasa 2 zakończyła obsługe {costume['name']}")
def kas_3():
    while True:
        print("Nowy Klient")
        costume = kolejka_3.get()
        print(f' [kasa 3] obsługuje {costume["name"]} który posiada {costume["product"]}')
        time.sleep(random.randint(3,7))
        print(f"kasa 3 zakończyła obsługe {costume['name']}")

def costumer_generator():
    while True:
        costumer = client ()
        size = [kolejka_1.qsize(), kolejka_2.qsize(), kolejka_3.qsize()]
        min_index = size.index(min(size))
        if min_index == 0:
            kolejka_1.put(costumer)
            print(f" {costumer} trafił do kasy 1")
        elif min_index == 1:
            kolejka_2.put(costumer)
            print(f"{costumer} klient trafił do kasy 2")
        else:
            kolejka_3.put(costumer)
            print(f"{costumer} klient trafił do kasy 3")
        time.sleep(random.randint(3,7))


threading.Thread(target= kas_1,daemon= True).start()
threading.Thread(target= kas_3, daemon= True).start()
threading.Thread(target= kas_2, daemon= True).start()
threading.Thread(target=costumer_generator, daemon=True).start()

time.sleep(60)
print("Koniec symulacki")