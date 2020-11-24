from PIL import Image

afbeelding = Image.open("tree.jpg")
afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height
helft_breedte =  afbeelding.width // 2 
helft_hoogte =  afbeelding.height // 2
nieuwe_size = (helft_breedte, helft_hoogte)
kleinere_afbeelding = afbeelding.resize(nieuwe_size)
kleinere_afbeelding.save('kleine boom.jpg')
