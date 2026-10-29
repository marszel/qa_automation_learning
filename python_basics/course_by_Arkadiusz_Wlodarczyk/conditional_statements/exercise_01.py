wynik = 0

i = 0
while i < 3:
    liczba = (int(input("Podaj dodatnią liczbę parzystą: ")))
    if liczba % 2 == 0:
        if liczba >= 0:
            wynik += liczba
            print(f"Obecny wynik: {wynik}")
        else:
            print("Podana liczba nie jest dodatnia. Wpisz poprawną liczbę ponownie: ")
            continue
    else:
        print("Podana liczbe nie jest parzysta. Wpisz liczbę ponownie: ")
        continue
    i +=1

print(f"Końcowy wynik to: {wynik}")