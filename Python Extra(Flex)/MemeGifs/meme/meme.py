
from PIL import Image, ImageFont,ImageDraw

achtergrond = Image.open("meme_background.jpg")
#background
breedte = achtergrond.width
hoogte = achtergrond.height

lettertype = ImageFont.truetype("impact.ttf", 50)
tekengebied = ImageDraw.Draw(achtergrond)

#teskt en tekts plaatising
tekst = "if i have to write 'hello world'\n               one more time"
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
tekst_x = (breedte - tekst_breedte) / 2

print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))
#tekst op de foto
tekengebied.multiline_text((tekst_x,10), tekst, font=lettertype, fill=(255,255,255))
achtergrond.show()
achtergrond.save("meme_met_tekst.jpg")
