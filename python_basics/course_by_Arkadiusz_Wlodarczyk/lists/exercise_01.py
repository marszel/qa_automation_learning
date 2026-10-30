imiona = ["Arkadiusz", "Wiola", "Antek"]

imie = input("Podaj imię: ").capitalize()

if imie in imiona:
    print("Dostęp przyznany.")
else:
    print("Brak dostępu.")

#------------------------------------------

if imie == "Arkadiusz" or imie == "Wiola" or imie == "Antek":
    print("Dostęp przyznany.")
else:
    print("Brak dostępu.")