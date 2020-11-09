import random
# random1= random.randrange(0, 10)
# random2= random.randrange(0, 10)
# random3= random.randrange(0, 10)
# random4= random.randrange(0, 10)
# while True:
#     print(random1)
#     print(random2)
#     print(random3)
#     print(random4)
    
#     andwoord= int(input("getal\n"))
#     if andwoord == random1 or andwoord == random2 or andwoord == random3 or andwoord == random4:
#         print("\ndood\n")
#     elif andwoord > 10:
#         print("kies een lager getal tussen 1 en 10")
#     else: 
#         print("\nleven\n")

random1= random.randrange(0, 10)
random2= random.randrange(0, 10)
random3= random.randrange(0, 10)
random4= random.randrange(0, 10)
cheat= 47
def loop_risk():
    andwoord= int(input("getal\n"))
    if andwoord == random1 or andwoord == random2 or andwoord == random3 or andwoord == random4:
        print("Je grijpt je vader bij de arm en begint te rennen van het gevaar.\nTerwijl jullie rennen hoor je het gevecht nogsteeds en zie je auto's rond je dorp.\nDe auto vuurt richting de groep bewapende mannen achter je.\nJe kijkt in de auto en ziet aan de kleding dat het soldaten zijn, Amerikaanse soldaten\nEen groep bewapende mannen met tagelmusten aan shieten op de auto en raken de soldaten.\nJe kan niet zo snel hun gezichten zien maar van 1 kan je zijn ogen herkennen.\nMaar van waar..")
        print("\nJe rent verder tot je buiten adem bent en het gevecht verder van je hoort.\nJou huis is niet ver van hier je kijkt naar je vader die al van vermoeitheid op de grond zit.\nJe verteld hem om snel op te staan en te kijken hoe het gaat met je je moeder(en zijn vrouw) die thuis bezord op ons wacht.")
        #consecuentie.....fk nederlands
        print("Je vader trekt even aan je. Je draait je om en op de grond zie je bloed. \nEen kogel ging langs zijn been en heeft zijn been verwond.\nJe tilt hem op en draag hem naar huis waar je moeder bezorgd op jullie wacht.")
        print("Je komt thuis en je moeder in in paniek door het bloed.\nZe pakt het first aid bakje dat jullie altijd bewaren en maakt de wond schoon eb zorgt ervoor.\nJij gaat naar je kamer en denk aan wat vandaag allemaal is gebeurt")
        print("Later roept je moeder je naar beneden.\nZe verteld dat de wond gelukkig niet erg was en dat de kogel maar langs ziojn huis nam en een hapje van zijn huid nam.")
    elif andwoord==cheat:
        print(random1)
        print(random2)
        print(random3)
        print(random4)
        loop_risk()
    else:
        print("Je grijpt je vader bij de arm en begint te rennen van het gevaar.\nTerwijl jullie rennen hoor je het gevecht nogsteeds en zie je auto's rond je dorp.\nDe auto vuurt richting de groep bewapende mannen achter je.\nJe kijkt in de auto en ziet aan de kleding dat het soldaten zijn, Amerikaanse soldaten\nEen groep bewapende mannen met tagelmusten aan shieten op de auto en raken de soldaten.\nJe kan niet zo snel hun gezichten zien maar van 1 kan je zijn ogen herkennen.\nMaar van waar..")
        print("\nJe rent verder tot je buiten adem bent en het gevecht verder van je hoort.\nJou huis is niet ver van hier je kijkt naar je vader die al van vermoeitheid op de grond zit.\nJe verteld hem om snel op te staan en te kijken hoe het gaat met je je moeder(en zijn vrouw) die thuis bezord op ons wacht.")
        #resultaat als je het goed heb.
        print("Jullie rennen het laatste stukje naar huis.\nTerwijl jou vader de situatie uitlegd ga je naar je kamer en bedenk je wat er net is gebeurt.")
        print("Je moeder roept je naar beneden om te praten.")
loop_risk()