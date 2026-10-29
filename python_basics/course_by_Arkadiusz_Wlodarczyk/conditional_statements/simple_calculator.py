a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

wybor = input("Wybierz: * - mnożenie, / - dzielenie, + - dodawanie, - - odejmowanie, ** - potęgowanie, % - modulo. Twój wybór: ")

if wybor == "*":
    print("Wynik mnożenia:", a * b)
elif wybor == "/":
    if b == 0:
        print("Nie wolno dzielić przez zero.")
    else:
        print("Wynik dzielenia: ", a / b)
elif wybor == "+":
    print("Wynik dodawania:", a + b)
elif wybor == "-":
    print("Wynik odejmowania:", a - b)
elif wybor == "**":
    print("Wynik potęgowania:", a ** b)
elif wybor == "%":
    print("Wynik modulo:", a % b)
else:
    print("Nie wybrałeś dostępnej opcji.")