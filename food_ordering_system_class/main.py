from food_ordering_system import Dish, Order, Restaurant

# Tworzymy dania
pizza = Dish("Pizza Margherita", 32.0)
burger = Dish("Cheeseburger", 27.5)
soup = Dish("Pomidorowa", 15.0)

# Tworzymy zamówienie i dodajemy dania
order1 = Order()
order1.add_dish(pizza)
order1.add_dish(soup)

order2 = Order()
order2.add_dish(burger)

# Tworzymy restaurację i dodajemy zamówienia
my_restaurant = Restaurant()
my_restaurant.add_order(order1)
my_restaurant.add_order(order2)

# Wyświetlamy wszystkie zamówienia
print("Lista zamówień:\n")
print(my_restaurant.list_orders())

# Wyświetlamy całkowity przychód
print(f"\n💰 Całkowity przychód: {my_restaurant.total_revenue()} zł")