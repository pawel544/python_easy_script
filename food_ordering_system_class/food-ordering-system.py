class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return (f"{self.name}, cena {self.price}")

class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        if dish:
            self.dishes.append(dish)
        else:
            print ("Nie wybrałeś dania")

    def total_price(self):
        return ( sum(dishe.price for dishe in self.dishes))

    def __str__(self):
        if not self.dishes:
            return( f"Klient nic nie zamówił")

        else:
            order_line = [f"- {dishe.name} ({dishe.price} zł)" for dishe in self.dishes]
            full= "\n".join(order_line)
            return f"Zamówienie :\n {full} \nSuma {self.total_price()}"

class Restaurant:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        if not order:
            print("Brak zamówienia")
        else:
            self.orders.append(order)

    def list_orders(self):
        if not self.orders:
            print(f"Brak zamówień do wyświetlenia")
        else:
            return "\n\n".join(str(order) for order in self.orders)

    def total_revenue(self):
        return sum(order.total_price() for order in self.orders)