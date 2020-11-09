import sys
import time
print("geef een naam en een getal en je klas")
def gesprek(naam, getal,klas):
    print(naam+":"+ " hallo mijn naam is "+ naam+ " ik ben "+getal +" jaar oud")
    time.sleep(2)
    print(naam+":"+"ik zit in klas "+ klas+" en wil me graag afmelden voor deze week vrijdag")  
    time.sleep(2)
    print("docent: "+"goede morgen "+naam+ " wat vervelend voor u ik hoop dat u snel beter word. ik zal u afmelden")
    time.sleep(2)
    print("docent: "+"doei")
gesprek(sys.argv[1], sys.argv[2], sys.argv[3])
