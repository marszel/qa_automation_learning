slownik = {"A": "Arbuz",
           "B": "Burza",
           "C": "Cebula"}

slownik["A"] = "Ananas"
print(slownik.get("A"))

slownik.update({"D": "Dynia"})

print(slownik)
del(slownik["D"])
print(slownik)
slownik.pop("C")
print(slownik)
slownik.popitem()
print(slownik)
len(slownik)
slownik.clear()
print(slownik)
