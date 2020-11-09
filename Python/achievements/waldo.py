  
import random
#list
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
#shuffel de list
random.shuffle(people)
#waldos positie
Waldo_pos= people.index("Waldo")
#print de lijst
print(people)
#print waldos positie
print("waldo's positie is "+ str(Waldo_pos))