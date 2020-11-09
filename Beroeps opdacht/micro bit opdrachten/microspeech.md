#Wat is geluid?
##Geluid in in simpele zin een hoorbare verandering van de luchtdruk.

#Wat is een lage toon? 
##geluid bestaad uit stilling, die stilling word gelezen in golfen. hoe hoger de gold hoe lager de toon.

#Wat is de hoogste frequentie die een vleermuis kan horen?
##100.000 Hz

#Kan geluid jouw gehoor beschadigen? Geef een voorbeeld.
##Bekende oorzaken ervoor zijn dat je teluid muziek luister maar er zijn ook zaken van ouderdom.
##gehoorschade houd in dat je oren en hersenen krijgen het simpelweg moeilijker om geluiden te verwerken.

#microbitt code:

# Add your Python code here. E.g.
from microbit import *
import speech
import random #import dat je random dingen kan selecteren en speech kan gebruiken
while True:
    randomwoordA= ["hello","AAAA","knop A"]
    randomwoordB= ["yo", "whats up", "knop B"]  #de twee arrays om random woorden van te halen
    scream= "AaAaAa"
    def speech(word):
        speech.say(word, speed=120, pitch=130, throat=100, mouth=200) #CODE VOOR DE TEKST   #atribbute error
        
    def speechselA():
        randomgetal= random.randint(0,3)
        display.show(randomgetal)               #code om een random woord te kiezen
        speech(randomwoordA[randomgetal])

    def speechselB():
        randomgetal= random.randint(0,3)
        display.show(randomgetal)               #code om een random woord te kiezen
        speech(randomwoordB[randomgetal])
        
    def scream(woord):
        speech.say(woord, speed=70, pitch=200, throat=50, mouth=200)  #tweede preset voor stem
        
    def speechselC():
        scream(scream)
        
    if button_a.is_pressed():
        speechselA()
    elif button_b.is_pressed():
        speechselB()
    

        
    