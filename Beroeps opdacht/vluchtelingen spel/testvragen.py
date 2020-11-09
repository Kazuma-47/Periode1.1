print("voer iets in")
hallo= ["a","b", "c"]
doei= ""
while doei not in hallo:
    doei = input("inonuwawad")
    if doei == "a":
        print("andwoord a\ndit is het een test")
    elif doei == "b":
        print("is b\ndit is het een test")
    elif doei == "c":
        print("is c\ndit is het een test")
    else:
        print("voer iets in\ndit is het een test")

#\n :is als <br> het slaat een regel voor je over.
#not in: geeft aan terwijl je andwoord niet iets in hallo is dan loopt hij het 
#dit word een combo tussen if else en while met een kleine set up van een array voor de andwoorden.


#dit is een voorbeeld waar ik de code van heb
# Setup

# response = ""
# while response not in yes_no:
#     response = input("Would you like to step into the forest?\nyes/no\n")
#     if response == "yes":
#         print("You head into the forest. You hear crows cawwing in the distance.\n")
#     elif response == "no":
#         print("You are not ready for this quest. Goodbye, " + ".")
#         quit()
#     else: 
#         print("I didn't understand that.\n")