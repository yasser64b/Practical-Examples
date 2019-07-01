import os
from PIL import Image, ImageFont, ImageDraw  # pip install pillow
# Have a font file in your directory like : Helvetica.ttf

def Add_date(pathIn, pathOut, text): 
    '''THis function dates images in a directory'''
    files = os.listdir(pathIn)
    for f in files:
        im = Image.open(pathIn+'/'+ f)
        d = ImageDraw.Draw(im)
        (x1,y1)=im.size
        font = ImageFont.truetype("Helvetica.ttf", size=int(0.025*x1))
        d.multiline_text((0.7*x1,0.95*y1), text, font=font, fill='blue', spacing=15, align="right")
        im.save(pathOut + '/' +'copy-' +f)

pathIn=  'C:/Users/Yasser Bigdeli/Dropbox/Python tutorials/16-Date your pictures/Images'
pathOut= 'C:/Users/Yasser Bigdeli/Dropbox/Python tutorials/16-Date your pictures/Images_labeled'
text='6/25/2019 California'
Add_date(pathIn,pathOut, text)
