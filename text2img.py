from PIL import Image, ImageDraw, ImageFont
import numpy as np

def text2img(text, size=(230, 300), ttf=None):
    # new white img
    img = Image.new('RGB', size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    # put the text on
    if ttf != None:
        font = ImageFont.truetype(ttf, 10, encoding='unic')
        draw.text((10, 0), text, font=font, fill=(0, 0, 0))
    else:
        draw.text((10, 0), text, fill=(0, 0, 0))
    return np.array(img), img

def zhtw2img(text, size=(230, 300), ttf='kaiu.ttf'):
    # remove the \n
    text = text.replace('\n', '')
    # add \n each 20 words
    text_seg = ''
    for i in range(len(text)):
        text_seg += text[i]
        if (i+1)%20 == 0:
            text_seg += '\n'
    return text2img(text_seg, size, ttf)