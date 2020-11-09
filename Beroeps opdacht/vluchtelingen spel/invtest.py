tas = ["brood", "geld", "papieren"]
hallo= ["a","b", "c"]
geld= 5000
print("\033[0;37;40m Normal text\n")
print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
doei= ""
while doei not in hallo:
    doei = input("actie?\nA. eet brood\nB. gooi 1 munt weg\nC. Scheur papier")
    if doei == "a":
        tas.pop(0)
    elif doei == "b":
        tas.pop(1)
        geld=geld-1
        print(geld)
    elif doei == "c":
        tas.pop(2)
    else:
        print("voer iets in\ndit is het een test")



print ('\n'.join(tas))



