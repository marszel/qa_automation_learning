imie = "Kasia"
nazwisko = "Kowalska"

pelne = imie + " " + nazwisko
print(imie + " " + nazwisko)

dlugi_string = """ To jest dlugi string 
To jest dlugi string 
To jest dlugi string 
To jest dlugi string 
To jest dlugi string 
"""

#LUB

dlugi_string = "To jest dlugi string\
To jest dlugi string\
To jest dlugi string\
To jest dlugi string\
To jest dlugi string"

print(imie[-1])
print(imie[:]) #całe imię
print(imie[1:3]) #ostatnie nie jest brane pod uwagę
print(imie[1:]) #od 1 do końca
print(imie[:3]) #od początku do 3 (bez 3)

pies = "reksio"
print(pies.capitalize())
print(pies.upper())
print(pies.lower())

a = input()
print(a + a)
a = int(a)

b = int(input()) #rzutowanie - zmiana jednego typu na drugi (float, int, string)

print(b + b)
print("Wynik dodawania to: " + str(a + b))

print("Kalkulator, który tylko dodaje")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
print("Wynik dodawania to: " + str(a + b))
print("Wynik dodawania", a, "+", b, "to:", a + b)
print(f"Wynik dodawania to: {a + b}")

name = input("What is your name? ")
color = input("What is you favourite color? ")
print(f"Hello {name}! Your favourite color is {color}.")
age = int(input("How old are you? "))
print(f"Next year you'll be {age + 1} years old.")