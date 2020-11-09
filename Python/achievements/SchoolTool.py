import datetime     #haalt de datum van vandaag


vandaag = datetime.datetime.now()       #haalt de benodigde info van de datum
print("de dag van vandaag is: ")

print(vandaag.strftime("%A"))       #print de dag van vandaag

if vandaag == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":   #als vandaag 1 van deze dagen is doet hij dit
    print ("is een schooldag dus begin je tas in te pakken.")
else:
    print("is weekend dus slaap lekker uit.")                           #als het niet 1 van die dagen zijn dan doet hij dit
