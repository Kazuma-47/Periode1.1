#vragen setup 
import time
import datetime
import random
abc=["A","B","C"]
ab= ["A","B"]
c=["C"]
geld= 6000
inv=[""]
shady=False
Rashid_enemie=False
inv.append(geld)
inv.append("Afghani")
vandaag= datetime.datetime.now()
maand=(vandaag.strftime("%B"))
week=(vandaag.strftime("%A"))
dag=(vandaag.strftime("%C"))
#vraag setup end
#start
print("DISCLAIMER: \nSTUKKEN VAN HET VERHAAL KOMEN MISSCHIEN NIET OVER MET HET DOCUMENT.\nDIT KOMT DOOR KLEINE AANPASSINGEN VOOR DE STORY EN CODE\nOOK IS DIT SPEL NOG NIET AF GEMAAKT WEGENS GEBREK AAN TIJD")
print("HET IS OOK AANGERADDEN OM DEZE GAME IN EEN LEGE MAP OP TE STARTEN VOOR EXTRA EASTEREGGS ;)")
print("VOOR DE BESTE ERVARING SPEEL DIT OOK IN FULL SCREEN CMD \n\n\n")
def start():
    
    print("Het land uit.")
    print("Start\nUitleg\nQuit")
    startknop=input("Maak je keuze\n").upper()
    if startknop== "START":
        time.sleep(1)
            
    elif startknop =="UITLEG":
        print("\nIn dit spel speel je als een vluchteling.")
        print("het doel is om je land uit te komen")
        print("Je maakt keuzes die impact op latere evenementen kunnen ")
        print("hebben en sommige die je zelf dood kunne maken.\n")
        start()
    elif startknop == "QUIT":
        quit()
    else:
        print("\nGeef de juiste input\n")
        start()
start()
#intro voor de game
#alinea 1
print("\n\n\n\n\n\n\nJe heet Adeel Abdella.\nJe bent 22 jaar oud en woon in een dorp in Afghanistan.\nJe woont met je moeder en vader en ben enigst kind.\nHet dorp bestaat uit kleine huisjes met van steen met een laag klei om het gebouw te isoleren.\nEr zijn ook veel straten van zand. Je dorp is in de buurt van de hoofdstad, daardoor komen vaak auto’s.\nDoor alle autos en mensen daar lopen heeft het zand een ander soort kleur gekregen en afval aan de randen \nvan alle inwwoners die dingen achterlaten.\n")
time.sleep(5)
#alinea 2
print("Je werkt op de markt met je ouders en verkoopt fruit en groente die jullie zelf groeien in de tuinen die jullie bezitten.\nJullie bent best bekend voor je goede qualiteit fruit en sinds het dorp niet zo groot is zijn er veel mensen die vaak fruit bij jou halen.\n ")
time.sleep(5)
#alinea 3
print("Het is vandaag "+ week +" "+ dag +" "+ maand+"\nJe verkoopt fruit met je vader.\nJe vader vraagt als je even wat water kon halen sinds hij dorst heeft.\nJe loopt naar een klein winkeltje een paar huisen verder en haalt wat\nwater voor je vader met het geld dat hij je heeft gegeven.\nje loopt een winkeltje in dat lijkt op een omgebouwd huis ziet een bekend gezicht.\n")
time.sleep(5)
#de meeting met rashid
print("Het is Rashid. Hij kwam daar om sigaretten te kopen.\nJullie zijn beide daar opgegroeid en kennen elkaar al sinds klein.\nSinds een paar dagen gedraagt hij zich best vreemd.\nJe ken hem al lang genoeg om te weten dat hij niet goed met stress omgaat en niet echt tegen druk kan.\n\n")
time.sleep(2)

#vraag 1
print("wat ga je doen?")
print("A. vraag hem als het met hem gaat en waarom hij zich zo gedraagt.\nB. groet hem snel en haal het water.")
andwoord_1= " "
while andwoord_1 not in ab:
    andwoord_1= input().upper()
    #resultaat process
    if andwoord_1 =="A":
        print("\nRashid neemt een moment om je vraag te beantwoorden.\nHij verteld je dat het niet zo goed gaat bij zijn werk en dat hij zich niet zo goed voelde.\nEen overduidelijke leugen.\n\nRashid helpt al een lange tijd zijn ouders met hun winkel en onze ouders kennen elkaar\nbest goed dus als daar iets miss mee was zouden wij het al weten.\nMaar je begrijp dat er iets is dat hij jou niet wilt vertellen dus je laat hem met rust en loop terug naar je vader.\n")
    elif andwoord_1 =="B":
        print("\nJe houd een kort gesprek met hem over hoe het met hem gaat en wat je hier doet en ga loop terug naar je vader. ")
    else:
        print("vul A/a B/b in.")

#tekst 2
#alinea 1
print("Onderweg terug hoor je mensen schreeuwen.\nHet komt van de plek waar jou kraampje zit.\n\nje arriveert bij je kraampje. Er is veel chaos, mensen rennen overal, en er is veel geschreeuw en lawaai.\nJe kijkt om je heen en ziet je vader om zich heen kijken met een blik van paniek.\nJe pers jezelf door de drukte heen en pak je vader vast.\nJullie rennen zo ver mogelijk van het lawaai en gevaar.\n" )


# clear screen loop
def csloop():
    print("\nbent u klaar met lezen? ")
    klaar= input().upper()
    if klaar == "YES" or klaar == "Y" or klaar == "JA":
        print("\nSTART INPUT EVENT...")
        #clear screen set up
        time.sleep(4)
        from os import system, name 
        #function om het scherm te whipen 
        def clear(): 
            if name == 'nt': 
                _ = system('cls') 
        clear()
    else:
        print("Voer yes in wanneer je klaar ben")
        csloop()
csloop()

#risk spel vactor spel intro
print("EVENT UITLEG: ")
print("\nDit word een event met puur geluk er zijn 4 getallen tussen 1 en 10 gekozen")
print("Als je 1 van de 4 random gekozen nummers heb gekozen zijn jullie in gevaar.")
print("als je een niet gekozen getal kiest dan zijn jullie veilig.")
#einde intro

#de 4 random getallen kiezen

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
        print("\n the magic number has been used :))")
        time.sleep(1)
        print("ACHIEVEMENT: NASTY CHEATER")
        achievement1=open("Cheats.txt","w+")
        achievement1.write("Ga je nou echt de script lezen en dan dit gebruiken om de uitkomt de krijgen... ik had meer verwacht ;)")
        achievement1.close()
        loop_risk()
    else:
        print("Je grijpt je vader bij de arm en begint te rennen van het gevaar.\nTerwijl jullie rennen hoor je het gevecht nogsteeds en zie je auto's rond je dorp.\nDe auto vuurt richting de groep bewapende mannen achter je.\nJe kijkt in de auto en ziet aan de kleding dat het soldaten zijn, Amerikaanse soldaten\nEen groep bewapende mannen met tagelmusten aan shieten op de auto en raken de soldaten.\nJe kan niet zo snel hun gezichten zien maar van 1 kan je zijn ogen herkennen.\nMaar van waar..")
        print("\nJe rent verder tot je buiten adem bent en het gevecht verder van je hoort.\nJou huis is niet ver van hier je kijkt naar je vader die al van vermoeidheid op de grond zit.\nJe verteld hem om snel op te staan en te kijken hoe het gaat met je moeder (zijn vrouw) die thuis bezord op ons wacht.")
        #resultaat als je het goed heb.
        print("Jullie rennen het laatste stukje naar huis.\n\nTerwijl jou vader de situatie uitlegd ga je naar je kamer en bedenk je wat er net is gebeurt.")
        print("Je moeder roept je naar beneden om te praten.")
loop_risk()
print("Ze leggen uit dat ze willen dat je een leven opbouw op in een betere omgeving. \nEn laten je een houten bakje zien met geld dat ze al voor 3 jaren hebben gespaart.\nHet moet wel genoeg zijn voor de reis naar een beter land. \nZe gaven je 2 weken om je te berijden voor je vertrek.\n")

# print("Wat wil je eerst doen?\nA. Groet je vrienden\nB. Pak je spullen\nC. Klaar voor vertrek!")
andwoord_2=""
while andwoord_2 not in c:
    andwoord_2= input("Wat wil je eerst doen?\nA. Groet je vrienden\nB. Pak je spullen\nC. Klaar voor vertrek!\n").upper()
    if andwoord_2=="A":
        print("\nje gaat naar Rashids huis en vraagt als hij thuis is om hem te groeten. Zijn ouders vertellen dat hij sinds gister niet thuis is geweest.\nJe ben een beetje ongerust erover maar hij kan voor zichzelf zorgen en gaat verder met afscheid nemen.\n\n")
    elif andwoord_2== "B":
        print("\nJe pakt 2 verschillende kleding stukken in zodat je zo min mogelijk spullen heb om te dragen en belangrijke papieren om jezelf te identificeren. \n")
        print("\nGAME NOTE:\nIn sommige situaties ga jij je invetaris kunnen gebruiken")
        print("Je kan het oproepen door inv of inventaris te typen bij de gegeven momenten.\n\n")
    elif andwoord_2== "C":
        print(" \n")
    else:
        print("vul uw andwoord in.")
#C gaat steeds opnieuw tot je C geef

print("Het is 5 uur in de middag, je gaat naar buiten om vervoer te zoeken om jou naar de hoofdstad te brengen")
print("Je loopt naar het plein die bekend staat voor de taxi’s.\nMensen komen daar vaak om het dorp uit te gaan. Maar er zijn altijd oplichters die je geld nemen en dan weg gaan.\nDaar tussen zijn er wel bekende taxi’s die je echt brengen maar die zijn meestal duurder.")

#taxi conversatie
print("\nJe loopt naar het plein en er staan 3 mannen.\nEen van ze praat met een mevrouw en de andere 2 kijken rond en zoeken naar klanten.\nJe zoekt oog contact op met de andere 2 mannen naast hem.\nZe wenken je om naar hun toe te komen. ")
print("Terwijl je naar hun toe loopt zie je ze discussiëren over iets.")
print("Je vraagt ze als 1 van hun je naar de hoofstad kunnen brengen.\n")
print("Ze beginnen met discussiëren over wie jou gaat brengen. \n")

print("Het zijn beide bekende taxis maar meestal zijn die duurder.")
print("De man die net in gesprek met de mevrouw was komt tussen hun.")
print("Voor 7 minuten worden ze aangesproken op hun gedrag\ndus je beslist even weg te lopen om voor andere opties te kijken.")
print("Net voordat je beslist naar huis te gaan loopt nog een man naar je toe.")
print("Random Man:'Ik hoorde dat je iemand zoekt om je naar de stad te brengen.' ")
print("Random Man:'Die sukkels daar zijn veel te duur en maken misbruik van hun reputatie.'")
print("Random Man:'Voor de juiste prijs kan ik- '")
print("Een van de mannen die je net aan spraken loopt naar je toe en onderbreekt julie conversatie.\nHij verteld dat hij je wel kan brengen en als je voor hem kiest is je eten drinken en onderdak allemaal geregeld.")
print("Ze laten jou de keuze maken...")

print("\nTIP:\nAls je je rijs geld wil checken dan doe C")
#beslissing
def plein2():
    import random
    import time
    global geld
    global inv
    global shady
    print("Welke Taxi kies je?\nA. De bekende taxi\nB. De onbekende man\nC. Inventaris ")
    andwoord_3=""
    while andwoord_3 not in abc:
        andwoord_3=input().upper()
        if andwoord_3 == "A":
            print("Je vraag aan de man als hij je naar de hoofdstad  kan brengen. ")
            time.sleep(2)
            print("Taxi: ‘Naar de hoofdstad huh? Dat is best wel ver van hier het gaat wel wat kosten.’")
            time.sleep(2)
            print("Adeel: hoeveel gaat het kosten?")
            time.sleep(2)
            print("Taxi: 300 Afgani")
            time.sleep(2)
            print("Adeel:Zoveel?" )
            time.sleep(2)
            print("Taxi: Ik zorg zelf voor ons eten en dat je een goeie slaap plek heb bij onze tussenstopjes")
            time.sleep(2)
            print("Klinkt dat goed?")
            time.sleep(2)
            vervoer =input("\nWilt u deze Taxi?\n Ja/Nee").upper()
            if vervoer=="YES" or vervoer== "Y" or vervoer ==" JA":
                geld=geld- 300
                print("\nEr werd 300 afghani afgetroken\nJe hebt nog "+ str(geld)+" over." )
            else:
                plein2()

        elif andwoord_3=="B":
            print("Je vraag aan de man als hij je naar de hoofdstad  kan brengen.")
            time.sleep(4)
            print("Taxi: ‘je wilt naar de hoofdstad? Dat kan ik doen voor de juiste prijs’")
            time.sleep(2)
            print("Adeel: hoeveel gaat het kosten?")
            time.sleep(2)
            print("Taxi: 200 Afgani")
            time.sleep(2)
            print("Taxi: Ik breng je daar binnen 2 dagen.")
            time.sleep(2)
            print("Goed?")
            vervoer=input("wat je jou andwoord? YES/NO").upper()
            if vervoer=="YES" or vervoer=="JA" or vervoer=="Y":
                geld=geld- 200
                print("\nEr werd 200 afghani afgetroken\nJe hebt nog "+ str(geld)+" over." )
                print("CODE RED EVENT: ")
                csloop()
                print("EVENT UITLEG: ")
                print("Dit is een spel om he reken skills te testen.")
                print("De som zal om de tavel van 5 draaien.")
                print("het spreekt voor zichzelf toch?")
                gd=input().upper()
                if gd== "YES" or gd== "JA" or gd=="Y":
                    print("mooi dan kunnen we beginnen")
                    print("Als je de som goed heb dan komt de taxi je morgen ophalen en word je niet opgelicht als je het fout heb dan ben je je geld\n kwijt en word je terug naar het plein gestuurd waar je de duurdere methode kan kiezen of opnieuw kan proberen ")  
                else:    
                    print("Dat is best jammer\nIk zal wel kijken als het mij kan boeien\nJe heb 5 seconde om je klaar te maken.")
                    print("Als je de som goed heb dan komt de taxi je morgen ophalen en word je niet opgelicht als je het fout heb dan ben je je geld\n kwijt en word je terug naar het plein gestuurd waar je de duurdere methode kan kiezen of opnieuw kan proberen ")
                time.sleep(5)
                random7= random.randrange(0, 10)
                randomget7= random.randrange(0, 5)
                andwoordsom= random7 * randomget7
                print("de som is: "+str(random7)+" * "+str(randomget7))
                som=int(input("Wat is het andwoord?"))
                if som == andwoordsom:
                    print('\nCorrect je komt ervoor nu mee weg.')
                    shady=True
                else:
                    print("\nIk had meer verwacht....\n Je hebt je geld verloren en je zag te taxi die je betaalde nooit terug")
                    plein2()
            else:
                plein2()
        elif andwoord_3 =="INVENTARIS" or andwoord_3 =="INV" or andwoord_3 =="C":
            print(inv)
            plein2()
        else:
            plein2()

#achivement
def plein():
    import random
    import time
    global geld
    global inv
    global shady
    print("Welke Taxi kies je?\nA. De bekende taxi\nB. De onbekende man\nC. Inventaris ")
    andwoord_3=""
    while andwoord_3 not in abc:
        andwoord_3=input().upper()
        if andwoord_3 == "A":
            time.sleep(4)
            print("Je vraag aan de man als hij je naar de hoofdstad  kan brengen. ")
            time.sleep(2)
            print("Taxi: ‘Naar de hoofdstad huh? Dat is best wel ver van hier het gaat wel wat kosten.’")
            time.sleep(2)
            print("Adeel: hoeveel gaat het kosten?")
            time.sleep(2)
            print("Taxi: 300 Afgani")
            time.sleep(2)
            print("Adeel:Zoveel?" )
            time.sleep(2)
            print("Taxi: Ik zorg zelf voor ons eten en dat je een goeie slaap plek heb bij onze tussenstopjes")
            time.sleep(2)
            print("Klinkt dat goed?")
            time.sleep(2)
            vervoer =input("\nWilt u deze Taxi?\n Y/N").upper()
            if vervoer=="YES" or vervoer== "Y" or vervoer ==" JA":
                geld=geld- 300
                print("\nEr werd 300 afghani afgetroken\nJe hebt nog "+ str(geld)+" over." )
            else:
                plein()

        elif andwoord_3=="B":
            print("Je vraag aan de man als hij je naar de hoofdstad  kan brengen.")
            time.sleep(4)
            print("Taxi: ‘je wilt naar de hoofdstad? Dat kan ik doen voor de juiste prijs’")
            time.sleep(2)
            print("Adeel: hoeveel gaat het kosten?")
            time.sleep(2)
            print("Taxi: 200 Afgani")
            time.sleep(2)
            print("Taxi: Ik breng je daar binnen 2 dagen.")
            time.sleep(2)
            print("Goed?")
            vervoer=input("wat is jou andwoord? Ja/Nee\n").upper()
            if vervoer=="YES" or vervoer== "Y" or vervoer =="JA":
                geld=geld- 200
                print("\nEr werd 200 afghani afgetroken\nJe hebt nog "+ str(geld)+" over." )
                print("CODE RED EVENT: ")
                csloop()
                print("EVENT UITLEG: ")
                print("Dit is een spel om he reken skills te testen.")
                print("het spreekt voor zichzelf toch?")
                goed=input().upper()
                if goed == "YES" or goed == "JA" or goed == "Y":
                    print("mooi dan kunnen we beginnen")
                    print("Als je de som goed heb dan komt de taxi je morgen ophalen en word je niet opgelicht als je het fout heb dan ben je je geld\n kwijt en word je terug naar het plein gestuurd waar je de duurdere methode kan kiezen of opnieuw kan proberen ")  
                else:    
                    print("Dat is best jammer\nIk zal wel kijken als het mij kan boeien\nJe heb 5 seconde om je klaar te maken.")
                    print("Als je de som goed heb dan komt de taxi je morgen ophalen en word je niet opgelicht als je het fout heb dan ben je je geld\n kwijt en word je terug naar het plein gestuurd waar je de duurdere methode kan kiezen of opnieuw kan proberen ")
                time.sleep(5)
                randomget1= random.randrange(0, 10)
                randomget2= random.randrange(0, 5)
                andwoordsom= randomget1 * randomget2
                print("de som is: "+str(randomget1)+" * "+str(randomget2))
                som=int(input("Wat is het andwoord?"))
                if som == andwoordsom:
                    print('\nCorrect je komt ervoor nu mee weg.')
                    shady=True
                else:
                    print("\nIk had meer verwacht....\n Je hebt je geld verloren en je zag te taxi die je betaalde nooit terug")
                    print("ACHIEVEMENT: No Math No Path!")
                    achievement=open("No Math No Path.txt","w+")
                    achievement.write("Kan niet een een som andwoorden....")
                    achievement.close()
                    plein2()
            else:
                plein()
        elif andwoord_3 =="INVENTARIS" or andwoord_3 =="INV" or andwoord_3 =="C":
            print(inv)
            plein()
        else:
            plein()
plein()
#Rijs BEGIN
if shady== False:
    print("\nJe spreekt de volgende dag af met de taxi om de rijs te beginnen.\nJe gaat de volgende ochtend naar de afgesproken plak van de taxi en stap in zijn busje. \nJe stapt zijn busje in. Het is best warm aar je kan best comfortabel zitten.\nJe krijg genoeg eten en vers water en om de paar minuten een plas plause en wat tijd om je benen te strekken.")
elif shady== True:
    print("\nJe spreekt de volgende dag af met de taxi om de rijs te beginnen.\nJe gaat de volgende ochtend naar de afgesproken plak van de taxi en stap in zijn busje.\nIn het busje zie je 4 andere mensen.\nTaxi:'Dit zijn andere clienten van mij ik hoop dat jullie goed met elkaar omgaan.'")
    print("Je zit met 3 andere mensen in een busje dat best wel krab is. \nJe krijg 1 maaltijd en 2 plas pauzes van 10 minuten waar je je benen ook kan strekken. ")
    print("In de bus is het warm, En iedereen sweet een beetje omdat het dicht op elkaar is\nmaar niemand zegt iets erover omdat het niet anders kan.")
    print("Om tijd te donen praten de mensen met elkaar. Maar voor het grootste deel van de rijs blijf jij stil")
    print("je voelt heimwee en denk aan hoe het met je vader en moeder gaat")
#aankomst dorp met omschrijving
print("\nHet begind donker te worden. In de avond is het moeilijk om te navigeren\ndoordat er geen straat lampen zijn van dorp naar dorp.")
print("Jullie stoppen bij een klein dorpje waar jullie gaan overnachten.")
print("Het dorp bestaad uit best wel veel huisjes, meer dan je gewend ben.")
print("sommige huisjes zijn iets meer luxe dan andere door materiaal en het \nis best druk op de dag.")
print("Er zijn winkeltjes en een markt waar mensen spullen verkopen.")
print("Ook waren er huisjes die je kon huren per nacht.")

#de aankomst bij het dorp
if shady==False:
    print("\nIn de avond komen jullie bij het dorp aan. ")
    print("Je stapt uit en ziet een klein huisje.")
    print("Het bestaad uit een keuken en 2 slaap kamers.")
    print("De slaap spullen zijn al klaar gezet.\n En het huis was best wel luxe met een gas keuken.")
    print("De taxi verteld je dat julie morgen vroeg weer vertrekken.")
    print("Hij gaat nog even weg om wat eten en drinken voor de rijs bij te vullen.") 
    print("Er waren twee bedden met dekens in het huis klaar voor gebruik.")

if shady ==True:
    print("\nIn de avond komen jullie bij het dorp aan. ")
    print("Je stapt uit en ziet 2 kleine huisjes.")
    print("In 1 huisje gaat de taxi bestuurder en jullie gaan in het ander")
    print("Jullie huis bestaad uit een kamer om te slapen en een toilet.")
    print("De avonden zijn best koud dus er waren al spullen klaar gezed voor jullie.\nEr waren niet genoeg dekens dus voor sommige moesten ze een deken delen of zonder slapen.")
    print("Er lagen wat matrassen op de vloer waar jullie op konden liggen.")

#Yasin introductie aan terrorisme
print("Het was best lastig om te slapen op een onbekende plek weg van iedereen die je kent.")
if shady==True:
    print("persoon: 'Hey, kan jij ook niet slapen?'")
    andwoord= ""
    Yasin_Boost= ""
    while andwoord not in ab:
        andwoord=input("Hoe andwoord je hem?\nA. Wie ben jij?\nB. Ik miss mijn thuis").upper()
        if andwoord=="A":
            print("Persoon: Oh juist.. ")
            time.sleep(1)
            print("Yanis:Mijn naam is Yanis. Ik kom van een dorp niet ver van die van jou.")
            print("Yanis: Ik ben sinds 4 dagen geleden op de vlucht voor een groep mensen.")
            print("Wat die mensen deden was gewoon fout.")
            vraag=""
            Yasin_Boost= True
            while vraag not in abc:
                
                vraag=input("\nA. Wat vrezelijk voor je\nB. ....\nC. Wie zijn ze?").upper()
                if vraag == "A":
                    #geld boost
                    
                    print("\nAdeel: 'Wat vrezelijk voor je ik kan me niet voorstellen hoe stressvol dit voor je is.'")
                    time.sleep(1)
                    print("Yanis: 'Ja dat zeker. Maar het was mijn keuze.\nToen ik ze voor het eerst zag voelde het zo rechtvaardig om me bij hun aantesluiten.'")
                    time.sleep(1)
                    print("Yanis: 'Maar al snel veranderde mijn beeld van hun.")
                    time.sleep(1)
                    print("Yanis: 'De manier hoe hun met mensen omgaan, hun methodes waren gewoon niet juist.'")
                    time.sleep(1)
                    print("Yanis: 'Ik ben voor hun een verrader dus je kan je voorstellen wat ze met mij doen als ze me te pakken krijgen.'")
                    time.sleep(1)
                    print("Yanis: 'Wees voorzichtig met wie je vertrouw in deze wereld.'")
                    time.sleep(1)
                    print("Yanis: 'Niet omdat iemand met je lacht betekend dat jullie vrienden zijn.'")
                    time.sleep(1)
                    print("Yanis: 'Het word laat. Het is beter als je nu een paar uren je ogen sluit. Morgen is weer een dag.'")
                elif vraag== "B":
                    print("\nAdeel: ...")
                    time.sleep(1)
                    print("Yanis: 'Het is zeker een vreselijke wereld daarbuiten huh?'") 
                    time.sleep(1)
                    print("Yanis: 'Ik ben een ten dood opgeschreven door de mensen die ik vertrouwde met mijn leven.'")
                    time.sleep(1)
                    print("Yanis: 'Ik ben dood maak niet uit waar ik ben. Ze hebben mensen overal.'")
                    time.sleep(1)
                    print("Daarom ga ik het land uit. Dat is de veiligste optie voor mij.")
                    time.sleep(1)
                    print("Adeel: ...")
                    time.sleep(1)
                    print("Yanis: 'Maar ja het begind laat te worden het is beter als we nu gaan rusten.'")
                    time.sleep(1)
                    print("Adeel:'Meneer Yas-'")
                    time.sleep(1)
                    print("Yasin: 'Noem mij maar Yasin. Je hoeft niet zo formeel tezijn'")
                    time.sleep(1)
                    print("Adeel: 'Waarom deelt u deze informatie met mij? Bent u niet bang dat ik u ook ga verraden?'")
                    time.sleep(1)
                    print("Yasin: 'Nee, Het maak niet echt uit wat je doet. Ik heb al een slecht gevoel over deze plek.\nBeter om mijn verhaal dan te delen vind je niet?'")
                elif vraag == "C":
                    print("\nAdeel: 'Wie zijn de mensen die achter u aan zitten?'")
                    time.sleep(1)
                    print("Yasin: 'Het is een terroristen groep die probeert in opstand te komen tegen de overheid om bepaalde omstandigheden te verbeteren.'")
                    time.sleep(1)
                    print("Yasin: 'Hoewel hun doel eigelijk goed is waren de manieren om aandacht te vragen niet goed.'")
                    time.sleep(1)
                    print("Yasin: 'Ze noemen zichzelf Jihad maar het zit nu vol met mensen die gewoon genieten van macht hebben over andere.'")
                    time.sleep(1)
                    print("Yasin: 'Ze namen alles van me. Ik heb 2 kleine jongens en een vrouw die in de hoofdstad op me wachten om samen het land uit te gaan.\n maar we werden uit elkaar gehaald toen we moesten vluchten.'")
                    time.sleep(1)
                    print("Maar het word laat. Laten we alle rust krijgen die we nodig hebben voor morgen.")
        elif andwoord== "B":
            Yasin_Boost=False
            #je krijg geen geld boost 
            print("\nAdeel: 'Ik miss mijn thuis.'")            
            print("persoon: 'Is dit jou eerste keer alleen reizen?'")
            print("Adeel: 'Ja ik ben zelf nooit uit mijn dorp geweest.'")
            print("persoon: 'Hey er is een eerste keer voor alles toch! hahaha.'")
            print("persoon: 'Wees gewoon voorzichtig. De wereld is als een roos.'")
            print("persoon: 'Het is mooi maar het heeft nogsteeds zijn stekels'")
            print("persoon: 'dus wees voorzichtig'")
            print("persoon: 'In elk geval probeer te slapen vandaag ja'")
        else: 
            print("Voer A of B in.")
#RIP Yasin
print("\nDe volgende ochtend barste een groep bewapende bemaskerde mannen het huis in.")
print("Iedereen sliep nog dus in shock keek je om je heen om te zien wat er aan de hand was.")
print("De mannen keeken rond alsof ze iets zochten.\n")
if Yasin_Boost== True:
    print("\nDe mannen schreeuwde dat niemand mocht bewegen.")
    print("Die stem... ")
    print("Je herkende die stem van ergends.")
    print("'Hij is hier!' Hoorde je in de hoek van de kamer.\nJe ziet de mannen Yasin mee slepen")
    hiro= ""
    while hiro not in ab:
        hiro=input("\nWat doe je nu?\nA. Kom op voor Yasin.\nB. Negeer de situatie en kijk weg.").upper()
        if hiro== "A":
            print("\nJe Probeerd op te staan maar een van de mannen slaan je tegen je hoofd met de achterkant van zijn wapen\n")
            print("Hij verteld je dat het beter is om te blijven ligen")
            echte_hiro= input("Wil je door gaan? Y/N").upper()
            if echte_hiro== "YES" or echte_hiro== "Y" or echte_hiro== "JA":
                print("Je hoofd doet pijn en voelt een warm gevoel langs je oog en wang vloeien.")
                print("je probeert toch op te staan en grijpt het wapen uit zijn hand")
                print("Een luide knal gaat af in de kamer.\nJe voelt iets warms over je heen komen alsof je op een wolle kussen ligt.\nJe voelt je slaperig\nHet voelt zo lekker en warm.\nAlsof je vooraltijd kon slapen")
                print("Langzamerhand verlies je je gedachtegang.")
                print("Je gaat dood.")
                print("ENDING: PLAYING HIRO")
                ending=open("Hero.txt","w+")
                ending.write("Onthou je doel van dit spel nou maar.\n EN WIE GAAT NOU MET HANDEN IN EEN WAPEN GEVECHT JE BENT GEEN JOHN WICK....\nwelp tenminste stierf je als een held i guess.")
                ending.close()
                quit()
            elif echte_hiro =="NO" or echte_hiro== "N" or echte_hiro== "NEE":
                print("iedereen in de kamer is bewapend.")
                print("Er valt niet veel voor hem te doen.")
                print("Hij zoekt oogcontact met jou en kijkt steeds naar zijn matras en dan weer naar jou.")
                print("Ze doen een zak over zijn hoofd en nemen hem mee.")
                print("Je wacht tot ze de kamer uit gaan met Yasin en ga gelijk naar zijn maras en kijkt eronder.")
                print("FILE ITEM OBTAINED: YANIS LETTER")
                ITEM=open("Yasins_Letter.txt","w+")
                ITEM.write("Als je mijn familie zie vertel ze dat ze alvast moeten gaan.\nDe jongens zijn vast bang dat ik nooit meer kom maar mijn vrouw is al voorbereid voor dit geval\nen wist dat dit zou gebeuren. \nBedankt. \nYasin\n PS: hier is een locatie waar mijn familie verblijft voor nu {Locatie}")
                ITEM.write("")
                ITEM.close()
                inv.append("Yasin's_Letter")
                print("\nDit item is leesbaar!")
                time.sleep(2)
                

elif Yasin_Boost == False:
    print("De mannen schreeuwde dat niemand mocht bewegen.")
    print("Die stem... ")
    print("Je herkende die stem van ergends.")
    print("'Hij is hier!' Hoorde je in de hoek van de kamer.\nJe ziet de mannen een persoon meeslepen met een zak over zijn hoofd om hem te verblinden.")
#De markt
print("\nNa dat nam iedereen even eem moment om bij te komen.")
print("Door dat moest de taxi ondervraagd worden dus had je nog een uur voor jezelf voor je zou vertrekken.")
print("Je beslist buiten van je omgeving te genieten en het beste ervan te maken.")
explore=""
while explore not in abc:
    explore= input("\nWaar wil je heen?\nA. Naar de markt en haal eten \nB. De omgeving van het dorp verkennen\n C. wacht bij het huis tot je weg moet").upper()
    if explore=="A":
        #Rashids dark secret
        print("Je loopt richting de markt. \nHet is best druk en levendig")
        print("De geur van eten vult je neus en geeft je een gevoel van thuis.")
        print("Je haalt iets te eten en tussen de groep ze je iemand die je beked voor komt een huisje uitlopen")
        print("Het is Rashid.")
        vraag= input("\nWat ga je nu doen?\nA. loop naar hem toe en vraag hem wat hij daar doet.\nB. negeer hem\n").upper()
        if vraag == "A" :
            print("Je loopt naar Rashid toe en tikt hem aan.")
            print("Rashid shikt wanneer hij jou ziet.")
            time.sleep(2)
            print("Radhid: 'Adeel wat doe je hier?'")
            time.sleep(2)
            print("Adeel: 'Ik zou jou hetzelfde willen vragen Rashid'")
            time.sleep(2)
            print("Rashid: Ik werk hier.")
            time.sleep(2)
            print("Adeel: 'Weet je niet beter dan om tegen je vriend te liegen.'")
            time.sleep(2)
            print("Rashid: 'Okay, volg mij'")
            time.sleep(2)
            print("Je volg Rashid naar een 2 verdieping gebouw.")
            time.sleep(2)
            print("\nHet is hier best druk met bewapende mensen.")
            time.sleep(2)
            print("je vraagt aand Rashid waar je ben")
            time.sleep(2)
            print("Ik werk hier. We zijn een groep rebellen die tegend de \noverheid strijden om een beter land te maken.\n We beschermen dorpen en de mensen voor een kleine prijs.")
            time.sleep(2)
            print("Rashid: 'Toen we in ons dorp waren werden we gevonden door een groep soldaten.\nWe moesten terug trekken naar dit dorp omdat het teveel voor ons werd.")
            time.sleep(2)
            print("Is iedereen okay'?")
            time.sleep(2)
            print("Een man komt binnen en Rashid verstijfd")
            time.sleep(2)
            print("Wie is deze jonge?")
            time.sleep(2)
            print("Rashid reageerd snel om te vertellen over wie je bent.")
            time.sleep(2)
            print("De mood in de kamer word slechter")
            time.sleep(2)
            print("man: 'Je weet toch wel dat je ons nu in gevaar zet door je kleine theekransje he?'")
            time.sleep(2)
            print("Wat als hij met ZE werkt? dan wat?")
            time.sleep(2)
            print("Rashid bied zijn excuses aan maar de man ziet er nog geiriteerder door.")
            time.sleep(2)
            print("Ze besluiten je op te sluiten in een cell")
            time.sleep(2)
            print("Het zag er uit net als in de films alleen het stonk enorm.")
            time.sleep(2)
            print("Naast je was er nog een cell met een man erin")
            time.sleep(1)
            print("In de andere kamer hoor je opeens geschreeuw.")
            time.sleep(1)
            print("Er was veel lawaai en beweging voor een tijdje en dan stilte")
            time.sleep(1)
            print("De deur voor je kamer gaat open.")
            time.sleep(1)
            print("Rashid loopt de kamer binnen.")
            time.sleep(1)
            print("Hij doet je cell open")
            time.sleep(1)
            print("Rashid probeert je te opverthuigen om je aan te sluiten bij de groep")
            time.sleep(1)
            print("Als je je nu aansluit betalen je goed en garandeer je jou families veiligheid. ")
            time.sleep(1)
            print("Alles wat je moet doen is nu een wapen pakken en meehelpen.")
            time.sleep(1)
            print("Je gaat uit je cell")
            time.sleep(1)
            print("Wat is je andwoord")
            andwoord= ""
            #ENDING 2
            while andwoord not in ab:
                andwoord=input("JA/NEE").upper()
                if andwoord =="JA":
                    print("Je sluit je aan bij de groep. Iedereen in het dorp was extra aardig tegen je omdat je hun\n‘beschermde’ je kreeg gratis eten en niemand sprak je tegen maar het voelde verkeerd.\nEen terroristische groep verlaten is niet zo makkelijk als het klinkt en het word vaak ook met\n grote consequenties vervolgd. Maar het gaat nu goed met je familie. Je vader en moeder\n verkopen hun fruit en je stuurt een keer in de zoveel tijd wat geld voor ze. Je verteld niks\n over waar het geld vandaag komt sinds dat een regel is maar je verteld hun dat je een once in a life time job heb gekregen.")
                    print("\nENDING: If you cant beat them join them")
                    Ending=open("TerrorEnding.txt","w+")
                    Ending.write("Je mag de terroristen joinen\n het zou best verleidelijk zijn sinds het nog thuis maar damn bro vriendschap maak echt niks uit")
                    Ending.close()
                    print("ACHIEVEMENT: EASY WAY OUT")
                    achievement3=open("Easy_Way_Out.txt","w+")
                    achievement3.write("Het was een simpele weg om je familie veilig en blij te maken maar is dit echt wat ze van je willen?")
                    achievement3.close()
                    print("Game over")
                    quit()
                elif andwoord == "NEE":
                    print("Je legt hem uit dat je je niet kan aansluiten. \nWat hij doet is verkeerd en de mensen zijn meer bang voor hun dan dat ze zich vellig voelen.\nRashid is niet zo blij erom en gedraagt zich vrij geïrriteerd naar je toe.\nHet lijkt wel een compleet ander persoon dan de Rashid die je kent.\nHij verteld je om weg te gaan en nooit terug te komen \nals hij je ooit nog ziet in een stad dan zullen mensen van zijn groep jou koud maken.")
                    print("Hij laat je weg gaan en verteld je dat de volgende keer dat hij je ziet het anders kan zijn.\n")
                    print("ACHIEVEMENT: Farewell")
                    achievement4=open("Farewell.txt","w+")
                    achievement4.write("Het was een goeie friendschap. Maar de goeie beslissing is altijd de moeilijkste.")
                    achievement4.close()
                    Rashid_enemie=True
                    print("Terwijl je naar buiten loop zie je de persoon die in de cell naast je zit.")
                    time.sleep(1)
                    print("het is yasin!")
                    time.sleep(1)
                    print("Hij zit onder het bloed.")
                    time.sleep(1)
                    print("Voor je iets kon zeggen zei rashid al dat hij nniet meer valt te redden.")
                    time.sleep(1)
                    print("Hij zal niet langer lijden wanneer ze terug komen")
                    print("Je probeerd Yasin gerust te stellen door te vertellen. Je verteld hem dat je voor ZE ga zorgen.")
                    print("\nJe loopt het gebouw uit met 1 friend minder.")
                    print("Je komt bij het huis aan.")
    elif explore == "B":
        print("Je loopt door het dorp.\nHet is een best mooi dorp, De huizen zijn best goed geisoleerd en er zijn veel mensen en verkeer die daar heen en weer lopen.\nDe huizen zijn met klei bedekt maar veel beter dan in het dorp.\n")
        print("Op straat heb je kinderen die voor hun deur spelen.\nDe zon schijnt vel en iedereen is buiten.")
        print("Je loopt rond en neemt je omgeving binnen tot het tijd is.")
    elif explore=="C":
        print("Je zit thuis en kan niet geloven wat er zojuist was gebeurt.\nJe gaat snel naar een winkeltje eten halen en blijft in het huisje tot de taxi terug is.")
#ariveer in de stad
print("De taxi komt bij het huisje.\nHij ziet er een beetje somber uit.")
print("Iedereen pakt zijn spullen en ruimt het huis leeg.")
print("Jullie stappen de taxi in en de rijs gaat verder.")

print("\nNa een lange dag aan in de auto zitten ariveren jullie eindelijk in de stad.")
print("Het is al avond.\nHet begind rustig te worden op straat.\nJe zoekt een plek om te rusten.\nJe vind een muurtje om tegen te leunen")
print("Je word wakker in de ochtend. De straat is best levendig")
#ending
if Yasin_Boost==True:
    print("Op de brief van Yanis stond een locatie van een persoon die hij goed kende. Daar verbleef zijn familie.\n")
    print("In de ochtend besloot je op zoek te gaaan naar die locatie. Je vond een taxi die je 130 afghani vroeg om je ernaar te brengen.")
    geld= geld-200
    print("\nJe ariveert bij de plek.")
    print("Je klopt op de deur, een man maakt het open en vraagt wie jij ben.")
    print("Je geeft de brief.\nHij sluit de deur.")
    print("Je loopt weg om wat eten te halen voor jezelf.")
    print("De markt hier is drukker dan elke plek die je tot nu toe heb meegemaakt. \nHet zit vol met mensen die dingen kopen, verkopen en zelfs met toeristen die het land willen zien.")
    if Rashid_enemie == True:
        print("Je ziet bewapende mannen lopen in je richting, inmiddels weet je ook al hoe de locale politie eruit ziet.\nHet zijn geen agenten.\nHun zijn dan met Rashid.")
        print("Volgends Rashid ben ik blijkbaar op hun lijst van mensen die ze gevangen moeten nemen.")
        print("Ze herkennen je en beginnen sneller naar je toe te lopen.")
        print("ALL OR NOTHING EVENT:")
        csloop()
        def memory():
            #setup
            print("Dit spel draait om memory ")
            print("Er komt een woord voor een seconde op het scherm \nben je er klaar voor?")
            andwoord=input("Ja/nee")
            if andwoord==  "JA":
                print("\nOkay maak je klaar hier komt hij dan")
                time.sleep(2)
            else:
                print("\nHad je niet van de vorige opdracht geleerd....het begind over 2 seconde")
                time.sleep(2)
            array1=["LINKS","RECHTS","BOVEN","ONDER","1","2","3","A","B"]
            levens=3
            score=0
            def clear(): 
                from os import system, name
                if name == 'nt': 
                    _ = system('cls') 
            while score == 3 or levens== 0:
                woord=random.choice(array1)
                print(woord)
                time.sleep(2)
                clear()
                w=input("wat stond net op het scherm?").upper()
                if w == woord:
                    print("\nCorrect")
                    score= score+1
                    print("Jou score van nu is "+str(score))     
                else:
                    print("Het andwoord is incorrect.")
                    levens=levens-1           
            if levens == 0:
                print("De mannen krijgen je tepakken.\nJe word opgesloten.")
            if score == 3:
                print("Je ontsnapt van de mannen")
    elif Rashid_enemie== False:
        print("Je loopt op de markt en haalt wat eten.")
        print("Een vrouw roept je en laat je naar binnen bij het huis waar je net was")
if Yasin_Boost==False:
    print("Vind een weg het land uit.")






