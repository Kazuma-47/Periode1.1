import os
bestand = open("test.txt", "r")
inhoud = bestand.read()
print("op het bestand heb ik dit geschreven")
print(inhoud)
bestand.close()


bestand2=open("klasgenoten.txt","r")
regel1 = bestand2.readline()
print(regel1)
regel2 = bestand2.readline()
print(regel2)

tekst_regel = bestand2.readline()
while tekst_regel:
    tekst_regel = tekst_regel.strip()
    print(tekst_regel)
    tekst_regel = bestand2.readline()
    
naam=""
hv=0
werkmap = os.getcwd()
print("De huidige map is: " + werkmap)
while hv ==0:
    naam= input("geef de naam van uw map aan")
    

    hv=len(naam)
    if hv > 0:
        os.mkdir(naam)
        print("komt eraan!")
    else:
        print("er is geen naam gegeven")
        
