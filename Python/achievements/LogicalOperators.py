print("voer een getal tussen 0 en 10")
begin_getal=int(input())
if begin_getal == 0 or begin_getal < 5:
    print("het getal is tussen 1 en vijf")
else:
    print("het getal is boven de vijf")
print("")
print("vul een getal 1 en 5 of 6 tot 10")
tweede=int(input())


if tweede > 0 and tweede < 5 or tweede > 6 and tweede < 10:
    print("dit is de and + or code")
else: 
    print("verkeerde getallen ingevuld")