stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"]
print("dit is de lijst: "+str(stuff))
print("\ndit zijn de strings: ")

stringlijst= []
for lijst in stuff:
    if type(lijst) is str:
        
        stringlijst.append(lijst)
print(stringlijst)

print("\n\nEn nu de int: ")

intlijst= []
for lijst2 in stuff:
    if type(lijst2) is int:

        intlijst.append(lijst2)
print(intlijst)

        #     print(lijst2)
print("\n\nde booleans: ")
boolijst= []
for lijst3 in stuff:
    if type(lijst3) is bool:
        boolijst.append(lijst3)
print(boolijst) 
        #     print(lijst3)
print("\n\nde floats: ")
floatlijst= []
for lijst3 in stuff:
    if type(lijst3) is float:
        floatlijst.append(lijst3)
print(floatlijst)
    #     print(lijst3)