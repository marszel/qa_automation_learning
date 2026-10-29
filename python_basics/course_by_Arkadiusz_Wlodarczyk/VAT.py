VAT = 23
obliczony_VAT = (1 + VAT / 100)
cena_netto_java = 10
cena_netto_ajax = 20

cena_brutto_java = cena_netto_java * obliczony_VAT
cena_brutto_ajax = cena_netto_ajax * obliczony_VAT

print(cena_brutto_java)
print(cena_brutto_ajax)
