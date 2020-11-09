

bestand2=open("klasgenoten.txt","r")
regel1 = bestand2.readline()
print(regel1)
regel2 = bestand2.readline()
print(regel2)

tekst_regel = bestand2.readline()
while tekst_regel:
    import os
    tekst_regel = bestand2.readline()
    os.mkdir(tekst_regel)

 
