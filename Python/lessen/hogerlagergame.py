def loop():
    import time
    import random
   
    getal= random.randrange(0, 47)
    random= random.randrange(0, 47)
    print ("het nieuwe getal is: " + str(getal))
    time.sleep(2)
    inp = str(input("is het volgende getal hoger of lager? H/L")).upper()
    
    if inp == "H" and getal > random :
        print("Het andwoor is goed het getal was kleiner")
        print("Het eerste getal was: "+ str(getal))
        print("het volgende getal was: "+ str(random))
        time.sleep(2)
        print (" ")
        loop()
    elif inp =="L" and getal < random :
        print("Het andwoord is goed het getal was kleiner")
        print("Het eerste getal was: "+ str(getal))
        print("het volgende getal was: "+ str(random))
        time.sleep(2)
        print (" ")
        loop()
    elif inp =="H" and getal < random:
        print("u hebt het fout het getal was kleiner")
        print("Het eerste getal was: "+ str(getal))
        print("het volgende getal was: "+ str(random))
        time.sleep(2)
        print (" ")
        loop()
    elif inp =="L" and getal > random:
        print("u hebt het fout het getal was groter")
        print("Het eerste getal was: "+ str(getal))
        print("het volgende getal was: "+ str(random))
        time.sleep(2)
        print (" ")
        loop()
    elif inp =="HELP":
        print(" ")
        print("het spel is simpel je krijgt een getal in het begin en je moet ")
        print("raden als het volgende getal hoger of lager is door met 'H' of'L' te reageren.")
        time.sleep(4)
        loop()
    elif inp == "QUIT":
         quit()
    else:  
        print(" ")
        print("Please type 'help' if you dont understand how this works.")
        print("type 'quit' if you want to leave.")
        print("voor meer info type 'help'.")
        loop()
        
loop()



