szukana_liczba = 55
liczba_uzytkownika = 0

while liczba_uzytkownika != szukana_liczba:
    try:
        liczba_uzytkownika = int(input("Zgadnij liczbę: "))
    except ValueError:
        print("To nie jest prawidłowa liczba. Spróbuj ponownie.")
        continue
    if liczba_uzytkownika > szukana_liczba:
        print(f"Szukana liczba jest mniejsza od {liczba_uzytkownika}. Spróbuj ponownie.")
    elif liczba_uzytkownika < szukana_liczba:
        print(f"Szukana liczba jest większa od {liczba_uzytkownika}. Spróbuj ponownie.")
    else:
        print("Brawo! Zgadłeś liczbę!")
        break