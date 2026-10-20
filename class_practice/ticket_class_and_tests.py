import random

class Ticket:
    def __init__(self, ticket_kind, ticket_price):
        self.kind = ticket_kind
        self.price = ticket_price

    # def buy_ticket(self, ?):
#         ?

class Customer:
    def __init__(self):
        names = ["Ela", "Marta", "Justyna", "Ola", "Olek", "Michał", "Dawid", "Juliusz", "Sławek", "Mariusz"]
        self.name = random.choice(names)
        self.age = random.randrange(10, 80)
        self.money = random.randrange(10, 60)

    def __str__(self):
        return f"Customer {self.name}, Age {self.age}, Money {self.money}"

class Zoo:
    def __init__(self):
        self.standard_ticket = Ticket("standard", 35)
        self.reduced_ticket = Ticket("reduced", 18)
        self.senior_ticket = Ticket("senior", 20)

    def sell_ticket(self, customer: Customer):
        if customer.age < 18:
            # customer.buy_ticket(ticket)
            if customer.money >= self.reduced_ticket.price:
                customer.money -= self.reduced_ticket.price
                print(f"{customer.name} (age: {customer.age}) bought {self.reduced_ticket.kind} ticket for {self.reduced_ticket.price} PLN.")
                return True
        elif 18 <= customer.age < 60:
            if customer.money >= self.standard_ticket.price:
                customer.money -= self.standard_ticket.price
                print(f"{customer.name} (age: {customer.age}) bought {self.standard_ticket.kind} ticket for {self.standard_ticket.price} PLN.")
                return True
        elif customer.age >= 60:
            if customer.money >= self.senior_ticket.price:
                customer.money -= self.senior_ticket.price
                print(f"{customer.name} (age: {customer.age}) bought {self.senior_ticket.kind} ticket for {self.senior_ticket.price} PLN.")
                return True

        print(f"{customer.name} has not enough money.")
        return False

# customers = [Customer() for c in range(10)]
customers = []
for c in range(10):
    customers.append(Customer())

zoo = Zoo()
for c in customers:
    if zoo.sell_ticket(c):
        print(f"{c.name}, have a great day in the ZOO.")
        print(c)
    else:
        print(f"Hey {c.name}, please come back with more money.")
