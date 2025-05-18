c1 = Customer("Paweł", "pawel@example.com")
c1.add_purchase(2, 100)
c1.add_purchase(1, 50)

manager = CustomerManager()
manager.add_customer(c1)
manager.list_customers()
print(manager.top_customer())
