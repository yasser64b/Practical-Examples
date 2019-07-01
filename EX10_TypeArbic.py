import arabic_reshaper #pip install arabic-reshaper 
from bidi.algorithm import get_display  # pip install python-bidi
from PIL import Image, ImageFont, ImageDraw # pip install pillow

text= 'سلام علیکم'
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)
im = Image.open("image1.jpg")
font = ImageFont.truetype("Sahel.ttf", size=190)
(x,y)=im.size
print(x,y)
d = ImageDraw.Draw(im)
d.multiline_text((2000,400), bidi_text, font=font, fill='yellow', spacing=15, align="right")
im.save(text+".png")