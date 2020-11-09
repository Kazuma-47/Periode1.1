zin=input("typ een zin.")
lijst= zin.split()
print (str(lijst))
for test in lijst:
    H=len(test)
    if H >= 3:
        stotter= test[0:2]
      
        print(stotter+".." +" "+ stotter+ ".." +test)

