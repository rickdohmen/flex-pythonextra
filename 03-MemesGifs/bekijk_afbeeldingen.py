from PIL import Image

afbeelding = Image.open("e06d8bd7e460ba5e7a2e09d0136d17bd.png")


afbeelding.show()


breedte = afbeelding.width
hoogte = afbeelding.height



print("de afbeelding" + str(breedte) + "pixels breed en" + str(hoogte)"hoog")



print(afbeelding.format, afbeelding.size, afbeelding.mode)
