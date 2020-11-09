verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

aantal= int(input("hoe veel km per maand rij je?"))

def kosten(km_per_maand):
    maandkosten = km_per_maand * liter_per_kilometer * benzine_kosten_per_liter 
    maandkosten2= maandkosten+ verzekering_per_maand
    print("je kosten voor deze maan zijn"+ str(round(maandkosten2, 2)))

check= type(aantal)
if check == int :
    kosten(aantal)
else :
    print("voer een getal in.")