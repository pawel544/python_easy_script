class Customer:
    def __init__(self, name, e_mail):
        self.name= name
        self.e_mail= e_mail
        self.purchase_history=[]
        self.amount_history=[]
    def add_purchase(self, amount, price):
        self.amount_history.append(amount)
        self.purchase_history.append(price)

    def total_spent(self):
        if len(self.purchase_history)>0:
            return sum(self.purchase_history)
        else:
            print( "Brak zakópów" )

    def average_purchase(self):
        if len(self.purchase_history)>0:

            return sum(self.purchase_history)/len(self.purchase_history)

        else:
            print( "Brak zakópów")
    def __str__(self):
        return(f" Imie:{self.name}, e-mail: {self.e_mail}, "
              f"lista zakópów: {self.amount_history}, lista cen, {self.purchase_history}")

class CustomerManager:
    def __init__(self):
        self.customers=[]
    def add_customer(self,customer):
        self.customers.append(customer)
    def find_customer_by_email(self,e_mail):
        for d in self.customers:
            if d.e_mail==e_mail:
                return (f"{d}")
        else:
            print (f"Brak klienta z podanym {e_mail}")
    def top_customer(self):
        if not self.customers:
            return ("Brak klientów w bazie")
        return max(self.customers, key= lambda c: sum(c.purchase_history))
    def list_customers(self):
        if not self.customers:
            return "Brak klientów"
        else:
            for customer  in self.customers:
                total= customer.total_spent()
                print (f"{customer.name}, {customer.e_mail} , wydał {total}")
            return ("Brak klientów")
