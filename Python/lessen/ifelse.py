A= 2
B= 4
C= 99
if A > 4:
    print("A is groter dan 4")
elif A < 4:
     print("A is kleiner 4")
elif A == 4:
    pass #dit laat de code niks doen
else:
    print("het is niet 4 maar " + str(A))

if A > B:
    print("a is groter dan B")
elif A==B:
    print("a en b zijn even veel")
elif A and B < C:
    print("a en b zijn kleiner dan C")
elif A < C and B < C :
    print("a en b zijn kleiner dan C")

print("einde!")