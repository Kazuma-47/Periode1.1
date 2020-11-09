#defs om de uitkomst van de if else te laten zien

def hebtijd():
    print("je ben nog optijd en kan lopen")
def busnemen():
    print("je neemt de bus")
def lopen():
    print("je loopt omdat je niet genoeg het voor een bus kaartje maar komt laat voor school.")
def huis():
    print("je gaat terug naar huis")
bus= 3
geld=0         #aanpasbaar
haast= True
optijd=False    #aanpasbaar
rennen= "snel"

regen= True             #aanpasbaar
geld_vergeten= False    #aanpasbaar
paraplu= False          #aanpasbaar

        #if else die alle var hierboven checked
if optijd == False:
    if haast ==True:
        if rennen == "snel":
            if geld > bus:
                busnemen()
            elif geld < bus:
                lopen()
                if regen == True and paraplu == False or geld_vergeten == True:
                    huis()

                else:
                    print("einde opdracht (error)")
else: 
    hebtijd()