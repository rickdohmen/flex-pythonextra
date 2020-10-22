from PIL import Image

afbeelding = Image.open("e06d8bd7e460ba5e7a2e09d0136d17bd.png")


afbeelding.show()


breedte = afbeelding.width
hoogte = afbeelding.height



helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save('e06d8bd7e460ba5e7a2e09d0136d17bd.png_klein.jpg')
