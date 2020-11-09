# def shuffle(stuk):
#      import random
     
#      shufflewoord= "".join(random.sample(stuk, len(stuk)))
#      print(shufflewoord)
#      vraag()
# def vraag():
#      woord= input("voer een woord in\n")
#      shuffle(woord)
# vraag()

def vraag():
     woord= input("voer een woord in\n")
     print(shuffle(woord))
def shuffle(stuk):
     import random
     return "".join(random.sample(stuk, len(stuk)))


while True:
     vraag()



