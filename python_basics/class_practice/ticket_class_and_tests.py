import random

class Ticket:
    def __init__(self, ticket_kind, ticket_price):
        self.kind = ticket_kind
        self.price = ticket_price

class Customer:
    def __init__(self):
        names = ["Lizzy", "Marry", "Justin", "Alex", "John", "Michael", "Sophie", "Bob", "Robert", "Mario"]
        self.name = random.choice(names)
        self.age = random.randrange(10, 80)
        self.money = random.randrange(10, 60)

    def buy_ticket(self, ticket: Ticket):
        if self.money >= ticket.price:
            self.money -= ticket.price
            print(f"{self.name} (age: {self.age}) bought {ticket.kind} ticket for {ticket.price} PLN.")
            return True
        print(f"{self.name} has not enough money.")
        return False

    def __str__(self):
        return f"Customer {self.name}, Age {self.age}, Money {self.money}"

class Zoo:
    def __init__(self):
        self.standard_ticket = Ticket("standard", 35)
        self.reduced_ticket = Ticket("reduced", 18)
        self.senior_ticket = Ticket("senior", 20)

    def sell_ticket(self, customer: Customer):
        if 0 <= customer.age < 18:
            return customer.buy_ticket(self.reduced_ticket)
        elif 18 <= customer.age < 60:
            return customer.buy_ticket(self.standard_ticket)
        elif 60 <= customer.age <= 120:
            return customer.buy_ticket(self.senior_ticket)
        else:
            print("Age has to be a number between 0 and 120.")
            return None

# customers = [Customer() for c in range(10)]
customers = []
for c in range(10):
    customers.append(Customer())

zoo = Zoo()
for c in customers:
    if zoo.sell_ticket(c):
        print(f"{c.name}, have a great day in the ZOO.")
    else:
        print(f"Hey {c.name}, please come back with more money.")
