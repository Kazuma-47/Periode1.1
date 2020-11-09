getal_1 = int(input("wat is jou eerste getal"))
getal_2 = int(input("wat is jou tweede getal"))


def math ():
    op= input("wat moet ik met de getallen doen")
    global getal_1
    global getal_2
    if op == "+":
        getal_1 +=  getal_2
        print(str(getal_1))
    elif op == "-":
        getal_1 -= getal_2
        print(str(getal_1))
    elif op == "/":
        getal_1 /= getal_2
        print(str(getal_1))
    elif op == "*":
        getal_1 *= getal_2
        print(str(getal_1))
    elif op == "%":
        ding= getal_1 % getal_2
        print(ding)
    elif op == "help":
        print("de mogelijke Operators zijn: ")
        print("optellen: +")
        print("aftrekken: -")
        print("delen: /")
        print("keer: *")
        print("geeft rest aan: %")  
        math()    
    else:
        print("voor alle opties kies 'help'." ) 
        math()
math()