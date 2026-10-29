wynik = 0

i = 0
for i in range (0,4):
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1

print("Wynik dodawania liczb to:", wynik)

# ------------------------------------------------------------------------------

for i in range (0,201):
    if i % 2 == 0:
        print(f"{i} jest liczbą parzystą.")
    else:
        print(f"{i} jest liczbą nieparzystą.")