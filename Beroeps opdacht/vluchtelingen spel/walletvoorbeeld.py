#vragen setup 
abc=["A","B","C"]
ab= ["A","B"]
geld= 5000
#vraag setup
print (geld)
def ding():
    global geld
    doei= ""
    while doei not in abc:
        doei = input("inonuwawad")
        if doei == "A":
            print("andwoord a\ndit is het een test")
        elif doei == "B":
            print("is b\ndit is het een test")
        elif doei == "C":
            geld=geld-1
            print(geld)
        else:
            print("voer iets in\ndit is het een test")
    print(geld)#geld var update
ding()
print(geld)
def ding2():
    global geld
    doei= ""
    while doei not in abc:
        doei = input("inonuwawad")
        if doei == "A":
            print("andwoord a\ndit is het een test")
        elif doei == "B":
            print("is b\ndit is het een test")
        elif doei == "C":
            geld=geld-1
            print(geld)
        else:
            print("voer iets in\ndit is het een test")
    print(geld)#geld var update
ding2()
print(geld)