lista_gosci_1 = {
    ("Arkadiusz", 28, "mężczyzna", "Kraków"),
    ("Wioletta", 25, "kobieta", "Warszawa"),
    ("Kuba", 32, "Mężczyzna", "Wrocław")
}

lista_gosci_2 = {
    ("Arkadiusz", 28, "męzczyzna", "Sopot"),
    ("Alicja", 40, "kobieta", "Rzeszów"),
    ("Włodzimierz", 50, "mężczyzna", "Gdańsk")
}

lista_gosci_3 = lista_gosci_1 & lista_gosci_2

for imie, wiek, plec, miasto in lista_gosci_1:
    print("Imię: ", imie)
    print("Wiek: ", wiek)
    print("Płeć: ", plec)
    print("Miasto: ", miasto)
    print("\n")