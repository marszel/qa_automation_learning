liczba = 100

while liczba >= 0:
    print(liczba)
    liczba -= 1

# ------------------------------------------------------------------------------

wynik = 0

i = 0
while i < 4:
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1

print("Wynik dodawania liczb to:", wynik)

# ------------------------------------------------------------------------------

wynik = 0

i = 0
while i < 3:
    x = int(input("Podaj dodatnią liczbę: "))
    if x > 0:
        wynik += x
    else:
        print("Liczba miała być dodatnia. Wpisz ponownie: ")
        continue
    print(f"Aktualny wynik dodawania to: {wynik}.")
    i += 1