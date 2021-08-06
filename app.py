from PIL import Image, ImageDraw, ImageFont

length = 16

if 15 <= length <= 17:
    x, y, shrift = 750, 1050, 180

img = Image.open('example.png')
d1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('akaya.ttf', shrift)
d1.text((x, y), "Ismoilov Abrorjon", font=myFont, fill =(255, 128, 0))

myFont = ImageFont.truetype('akaya.ttf', 60)
d1.text((700, 1555), "7 March 2021", font=myFont, fill =(255, 128, 0))
d1.text((1755, 1555), "by @mrsolijonov", font=myFont, fill =(255, 128, 0))

img.show()
img.save("images/Abrorjon.png")
