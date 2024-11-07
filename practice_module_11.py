from PIL import Image
from PIL import ImageDraw, ImageFont


def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_photo('photo.jpg')
im_2 = new_photo('sun.jpg')

w, h = im.size

im.paste(im_2, (50, 50))

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('BookLightRegular.ttf', 30)
draw.text((500, 200), 'TIGER&SUN', font=font, fill='red')
im.show()
