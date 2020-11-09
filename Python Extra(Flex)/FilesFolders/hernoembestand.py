import os

bestsnaam = "demobestand.txt"

map_ding = os.getcwd()

pad = os.path.join(map_ding, bestsnaam)
print("Dit bestand gaan we hernoemen: " + pad)

nieuwe_naam = input("Nieuwe bestandsnaam: ")

if len(nieuwe_naam) > 0:
    nieuwe_volledige_pad = os.path.join(map_ding, nieuwe_naam)
    print("Bestand wordt hernoemd naar: " + nieuwe_volledige_pad)
    
    os.rename(pad, nieuwe_volledige_pad)
    print("Bestand hernoemd")
else:
    print("Sorry, geen geldige invoer, einde programma")
