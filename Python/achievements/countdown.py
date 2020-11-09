import time
import os
getal = 1
while getal < 1000:
  print(getal)
  time.sleep(1)
  getal += 1
print("JE HEB JE TIJD VERSPILD YAAAAAY")
time.sleep(2)                      #open() staat zodat je een file in de zelfde map wil openen
filestuk = open("reward.txt", "r") #reward is de file name en R is de method (wat je met de file wil doen R staat voor read)

print(filestuk.read())      #read laat je elke line printen