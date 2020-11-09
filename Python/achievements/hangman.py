#hangman
#maak een array -kies een string- maak de string een array
#regels zijn 1 letter als je meer doet dan krijg je waring en opnieuw de keuze
#als je klaar ben doe quit() met een you win of you loose



#setup
import time
def csloop():
    print("\nwilt u het scherm opruimen?Y/N ")
    klaar= input().upper()
    if klaar == "YES" or klaar == "Y" or klaar == "JA":
        from os import system, name 
        #function om het scherm te whipen 
        def clear(): 
            if name == 'nt': 
                _ = system('cls') 
        clear()
    else:
        print("\ndan zal alle text blijven\n\n")

import random
woorden=["DRINKEN","DOEI","CODE"]
levens=6
juist=[]
fout=[]
#einde Setup
#intro
print("Dag speler\nWelcome bij mijn hangman spel\n")
print("de regels zijn simpel\n-Je mag 1 letter per ronde invoeren\n-Als je alle letters of het hele woord raad win jij\n-Als je Hangt win ik\n\nBen je ready?\nYes/No")
ready= input().upper()
if ready == "YES":
    print("\nMooi! later we beginnen.")
elif ready == "NO":
    print("Okay je kon zoizo niet aan...doei!")
    quit()
elif ready == "CHEAT":
    print("\nSinds je het niet aankan geef ik je een tip.\nDe woorden die je kan kiezen zijn:\nhallo\ndoei\ncode\n\nsucces met het spel!!")
else:
    print("Voer AUB Yes of No in")
#einde intro
#woord setup
woord_selectie = random.choice(woorden)
array= list(woord_selectie)
lengte= len(array)
#einde setup
print("Het woord heeft "+str(lengte)+" letters.")

invoer=""
    #keuze maken en dan een if else voor alle inputs 
while juist not in array:
    print("In gevoerde foute letter: "+ str(fout))
    print("Juist in gevoerde letters: "+str(juist))
    print("levens: "+str(levens))
    invoer=input("\n Voer een letter in \nTip: typen voor een hint over het woord voer 'TIP' in\n").upper()
    test=list(invoer)
    woordlengte= len(test)
    error= False
    if invoer == "TIP":
        if woord_selectie=="DRINKEN":
            print("Je consumeert het voor hydratie")
        elif woord_selectie== "DOEI":
            print("\nwat zeg je als je iemand groeten\n")
        elif woord_selectie== "CODE":
            print("\nHet zit elke script die je schrijf\n")    
        error=True
    elif invoer == "47":
        print(woord_selectie)
        error= True

    elif woordlengte== 2:
        print("\nVoer 1 character in!")
        error= True
        csloop()
        error== True
    if invoer in juist:
        print("Deze letter is al opgegeven\n")
        print(juist)
        csloop()
    if invoer in array:
        print("Correct")
        juist.append(invoer)
        print(juist)
        csloop()
    elif invoer in fout:
        print("\nDeze letter is al op gegeven")
        print("Je heb "+str(levens)+ " over\n")
        csloop()
   
    if invoer not in array and invoer not in fout and error== False:
        print("fout")
        fout.append(invoer)
        print("alle ingevoerde letters: "+ str(fout))
        levens=levens-1
        print("\n je hebt "+str(levens)+" levens over\n")
        csloop()
    
    if juist == array:
        print("YOU WIN")
        print("Het gekozen woord was "+woord_selectie)
        quit()
    if levens== 0:
        print("\nGAME OVER!")
        print("Het gekozen woord was "+woord_selectie)
        print("out of lives")
        quit()
