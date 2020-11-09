# print("Hallo, Ik ben João")
# print("Ik hoop dat met deze vragen lijst jullie mij beter leren kennen.")
# def vraag_1 ():
#     print("waar wil je over weten?")
#     print(" ")
#     print("1. De verschilende leeringen")
#     print("2. De leeraren")
#     print("3. vorige ervaring met code")
#     andwoord_1= str(input())
#     # zet dat andwoord 1 in hoofdletter word
#     if andwoord_1 == "1":
#         print(" ")
#         print("Er waren verschilende mensen die ik tegen kwam op de school het was erg leuk en ik genoot van mensen ontmoeten die zichzelf waren.")
#         vraag_2()
#     elif andwoord_1== "2":
#         print(" ")
#         print("Er waren veel leuke leeraren. Ze leken wel veel te genieten van hun baan .")
#         vraag_2()
#     elif andwoord_1 == "3":
#         print(" ")
#         print("ik had voor deze opleiding web design gedaan op ROC Hilversum.")
#         vraag_2()
#     elif andwoord_1 == "help":
#         print("als u een hoofdstuk wilt lezen kunt u de nummers typen die bij de info horen die u wilt.")
#         print("als u wilt stoppen typ 'quit'")
#         vraag_2()
#     elif andwoord_1 == "quit":
#         quit()
#     else:
#         print("typ 'help' als u niet begrijp hoe het werkt")
# vraag_1()

def vraag_1():
    print("je komt de klas binnen en iedereen kijkt naar je.")
    print("wat doe je?")
    print("A. Groet netjes en leg uit waarom je telaat ben.")
    print("B. Groet netjes en ga galijk naar je plek en wacht to de leeraar je vraagt waarom je telaat ben.")
    print("C. Zeg geen woord en loop de klas in.")
    

def intro():
    print("je loopt naar binnen en ga naar de receptie. alle lessen zijn al begonnen en je zou je zou vandaag je klas ontmoeten")
    print("de vrouw verteld je de weg naar je klas.")
    vraag_1()
def start():
    input_1=input()
    if input_1== "play":
        import time
        time.sleep(1)
        intro()
    elif input_1=="uitleg":
        import time
        print("Je speelt als een leerling Op MA COllege en je ben nieuw")
        print("het doel is om vrienden te maken.")
        print("en de school te leren kennen")
        time.sleep(2)
        begin()
    elif input_1=="quit":
        quit()


def begin():
    print("")
    print("Media College leren kennen")
    print("play")
    print("uitleg")
    print("quit")
    start()
begin()
andwoord= str(input()).upper()
def vraag_4():
    print("In de klas steld de meester je een vraag")
    print("jij weet het andwoord niet")
    print("de mensen die je in de pause zag ging zitten geven je een shouder duw en vertellen het andwoord")
    print("na de les gingen jullie samen naar huis...")
    print("print you win je heb vrienden gemaakt")
#into 2
def vraag_2():
    global andwoord
    if andwoord == "A":
     
        print("de les is voorbij en een persoon vraagt je als je met hem wilt lunchen. jullie lunchen samen en praten over dingen die jullie leuk vinden")
        print("hij introduceert je ook een zijn groep vrienden die hij voor deze school al kende.")
        
        Ja= input("blijf je met hun hangen? Y/N").upper()
        if Ja== "Y":
            print("jij heb 3 vrienden gemaakt")
            print("na de pause gaan jullie weer naar de les")
            vraag_4()
        else:
            print("Game Over je hebt geen vrienden gemaakt")
    elif andwoord== "C":
      
        print("een paar mensen na de les vragen je om met hun buiten te hangen.")
        print("jullie zitten buiten en praten over dingen die je leuk vind.")
        
        ja= input("blijf je met hun hangen? Y/N").upper()
        if ja== "Y":
            print("jij heb 3 vrienden gemaakt")
            print("na de pause gaan jullie weer naar de les en gaat de dag verder")
            vraag_4()
        else: 
            print("Game Over je hebt geen vrienden gemaat")

def vraag_3():
    print("de persoon tikt je aan.")
    print("je draait je om en ziet een jonge die je een blaadje naar je wijst.")
    print("het zijn les notaties. 'bedank me later' hoor je van achter je")
    print("na de les bedank je hem. hij vraagt als je met hem wilt lunchen.")
    ja= input("blijf je met hun hangen? Y/N").upper()
    if ja== "Y":
        print("jij heb 1 vriend gemaakt")
        print("jullie lunchen samen en gaan na de pause naar de klas.")
        vraag_4
    else: 
        print("Game Over je hebt geen vrienden gemaakt")   

if andwoord == "A":
    print("")
    print("je verteld dat het je spijt dat je telaat ben en gaat zitten. de meester gaat verder met de uitleg")
    
    vraag_2()
elif andwoord=="B":
    print("")
    print("je groet de klas en zit op een random lege plek.")
    print("iemand tikt je aan...")

    vraag_3()
elif andwoord=="c":
    print("")
    print("de meester kijk afkeurend naar je maar je trekt je er niks van aan en gaat verder naar je plek.")
    vraag_2()
else:
    print("")
    print("AUB geef A,B of C aan")
    vraag_1()





