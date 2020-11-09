bomen_totaal= 333
shadowtree= bomen_totaal/3*2
sun_trees= bomen_totaal- shadowtree
print(str(shadowtree)+" bomen staan in de shaduw en "+str(sun_trees) +"staan in de zon")

sun_drops_1= 146
print(str(sun_drops_1)+" apples geeft een boom in de zon")

shadow_drops_1=int(146/100*80)
print(str(shadow_drops_1)+ " apples geeft een boom in de schaduw")

total_sundrops= sun_drops_1* 111
print(str(total_sundrops)+ "apples geven de bomen in de zon in totaal")

total_shadowdrops=shadow_drops_1 * 222
print(str(total_sundrops)+ " apples geven de bomen in de schaduw in totaal")

total_drops=total_shadowdrops + total_sundrops
ik= int(total_drops/4) 
print("ik mag "+ str(ik)+ " verkopen")