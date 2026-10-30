lista_owoce = ["jabłko", "banan", "śliwka", "truskawka", "banan", "gruszka", "malina"]

def test_metody(wartosc, zawartosc):
    if wartosc == zawartosc:
        print("Pass")
    else:
        print("Fail")

test_metody((len(lista_owoce)), 7)

lista_owoce.append("jagoda")
test_metody(lista_owoce[-1], "jagoda")

lista_owoce.extend(["kiwi", "melon"])
test_metody(lista_owoce[-1], "melon")
test_metody(lista_owoce[-2], "kiwi")

lista_owoce.insert(0, "pomarańcza")
test_metody(lista_owoce[0], "pomarańcza")

test_metody((lista_owoce.index("śliwka")), 3)
