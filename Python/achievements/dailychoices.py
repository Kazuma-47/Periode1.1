# defs
aura_ball= 5
earth_ball=7
heal= 16
hp_you= 40
hp_monster= 50
monster_Atc= 3
def turn():
        global hp_you
        global hp_monster
        hp=hp_you
        hpm=hp_monster
        print("Your Hp: "+str(hp))
        print("monster HP is: "+str(hpm))
        print("your attacks are: ")
        print("Aura ball")
        print("earth ball")
        print("ARMAKITTON(als je niet kan winnen)")
        print("heal")
        print("")
        attack=input().upper()
        if attack== "AURA BALL":
            hp_overm=hp_monster-aura_ball
            print("monster heeft hp over: "+str(hp_overm))
            hp_me=hp_you-monster_Atc
            print("jij heb "+ str(hp_me) +" hp over")
            turn()
        elif attack== "HEAL":
            hp_you=+heal
            print("you healed. your hp is now: "+str(hp_you))
            hp_me=hp_you-monster_Atc
            print("jij heb "+ str(hp_me) +" hp over")
            turn()
        elif attack=="EARTH BALL":
            hp_overm=hp_monster=-earth_ball
            print("monster heeft hp over: "+str(hp_overm))
            hp_me=hp_you-monster_Atc
            print("jij heb "+ str(hp_me) +" hp over")
            turn()
        elif attack=="ARMAKITTON":
            print("je hoefde niet zo overkill tegaan maar je gooit met al je kracht een kat naar zijn hoofd.")
            print("die kat veranderd in een monster en eet het andere monster op en verandert snel terug alsof er niks is gebeurt.")
            print("YOU WIN")
        else:
            print("geef een attack aan")
            print("")
            turn()
        if hp ==0:
            print("je ben dood")
        elif hpm == 0:
            print("you win")
def battle():
    turn()
    
def stuk_2():

    print("je stapt naar buiten en je buurman zwaait naar je.")
    print("wat doe je?")
    print("")
    print("A. je zwaait terug en en groet hem netjes terwijl je naar buiten loop en je deur opslot doe.")
    print("B. Je wijst je middelvinger en draat weg van hem.")
    print("C. je zwaait naar hem en inspect hem.")
    andwoord_2=input().upper()
    if andwoord_2== "A":
       
        print("Je groet je buurman netjes en loopt richting het park maar voel alsof je iets vergeet.")
        print("bij je deur zie je je huisdier naar je kijken.")
        print("Je had hem gister belooft naar het park te brengen.")
        print("je doet je deur open en neemt je huisdier mee")
        print("je voelt iets vreemd en kijk naar links")
        print("je buurman muteerd in een beest waar je mee moet vechten")
        battle()
    elif andwoord_2=="B":
       
        print("uit iritatie muteerd je buurman in een beest en moet je met hem vechten")
        print("tf is wrong with you btw...")
        battle()
    elif andwoord_2=="C":
        
        print("Je zwaait meer je merkt dat iets op je buurman zijn arm zit.")
        print("je buurman zwaaide niet naar je maar hij probeerde iets van zijn arm af te halen.")
        print("zijn levends aura gaat zwaar omhoog en word wild.")
        battle()


# einde defs
# eerste actie
print("je word wakker wat doe je eerst")
print("A. je staat op")
print("B. je blijft voor 15 minuten liggen")
andwoord= input().upper()
if andwoord == "A":
    print("je staat op uit je bed en bedenk wat je als volgende wilt doen")
elif andwoord== "B":
    print("je doet je ogen nog voor 10 minuten dicht terwijl je wacht ")
else:
    print("invalid input")

# tweede actie
if andwoord == "A":
    print("Je maak ontbijt en maak je daarna klaar om naar buiten te gaan")
    stuk_2()
elif andwoord == "B":
    print("Na even je ogen dicht doet word al snel weer wakker gemaakt door het gevoel van iets dat op je springt. ")
    print("Het was je huisdier.")
    print("hij wou naar buiten om te wandelen sinds je het gister al had belooft")
    stuk_2()

print("")


        