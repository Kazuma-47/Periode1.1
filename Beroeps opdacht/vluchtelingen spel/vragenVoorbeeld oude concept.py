def vraag_1():

    print("wat doe je?")
    print("A. Neem de telefoon op")
    print("B. Hang de telefoon op")
    print("C. Bel later terug")
    

def intro():
    print("Jou naam is Adeel Abdalla, je woont in Kabul de hoofdstad van Afghanistan")
    print("Je werkt voor de overheid en leeft een normaal leven.")
    print("Je telefoon trilt. je word gebelt door een onbekend nummer")
    vraag_1()
def start():
    if input_1== "play":
        import time
        time.sleep(1)
        intro()
    elif input_1=="uitleg":
        print("In dit spel speel je als een vluchteling.")
        print("het doel is om naar Amsterdam te komen")
        print("Je maakt keuzes die impact op latere evenementen kunnen ")
        print("hebben en sommige die je zelf dood kunne maken.")
        start()
    elif input_1=="quit":
        quit()



print("Vluchtelingen spel")
print("play")
print("uitleg")
print("quit")
input_1=input()
start()

andwoord= input()
#into 2
def vraag_2():
    global andwoord
    if andwoord == "A":
        print("")
        print("Dit is de eerste keer dat zoiets gebeurt. De persoon hangt op en je gaat verder met je werk.")
        print("Je hebt een slecht gevoel en voelt je een beetje paranoide om je omgeving. Met elk onbekend geluid draai je je om.")
        print("Om 8 uur in de s'avonds ben je klaar met je werk en loopt je  naar je auto op de parkeer plaats. Je gaat het gebouw uit en je hoort een knal.")
        print("Het kwam van het parkeer terein. je rent ernaartoe en ziet dat jou auto is opgeblazen.")
    elif andwoord == "B":
        import time
        print("")
        print("Om 8 uur in de s'avonds ben je klaar met je werk en loopt je  naar je auto op de parkeer plaats.")
        print("terwijl je op het parkeer plaat naar je auto loop zie je een explosie in de buurt van waar je auto was.")
        time.sleep(1)
        print("je auto is onploft.")
    elif andwoord== "C":
        import time
        print("Het is 8 uur en je ben klaar met je werk. Je  besluit je je telefoon te pakken en het numer terug te bellen.")
        print(". . .")
        time.sleep(2)
        print("Het numer is niet meer in gebruik. Had je het verkeerde numer?") 
        print("je check je berichten om een voice mail te vinden.")
        print("Een man schreeuwd in je oor. Maar je kan amper verstaan wat hij zegt.")
        print("Hij zegt dat je ontslag moet nemen anders komen ze jou en je familie afmaken.")
        print("terwijl je luister loop je alvast naar je auto op de parkeer is maar word snel onderbroken door een explosie in de buurt van je.")
        print("je checked je omgeving en ziet dat het in de buurt van je auto is.")
        print("je rent ernaar toe en ziet je vernielde auto.")
        print("je auto is onploft.")

if andwoord == "A":
    import time
    print("")
    print("Een man schreeuwd in je oor. Maar je kan amper verstaan wat hij zegt.")
    time.sleep(0.5)
    print("Hij zegt dat je ontslag moet nemen anders komen ze jou en je familie afmaken.")
    vraag_2()
elif andwoord=="B":
    print("")
    print("je haalt je telefoon uit je zak en hang op. en ga verder met je dag")
    vraag_2()
elif andwoord=="c":
    print("")
    print("Je haalt je telefoon uit je zak en hangt op. Later bel je terug maar het nummer was niet in gebruik")
    vraag_2()
else:
    print("")
    print("AUB geef A,B of C aan")
    vraag_1()





