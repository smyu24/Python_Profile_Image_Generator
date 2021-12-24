
import random
from PIL import Image, ImageDraw

def lines():
    """LINES: # draw.line(xy, fill=None, width=0)
    img = Image.new('RGB', (500, 300), (125, 125, 125))
    draw = ImageDraw.Draw(img)
    draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)"""
    with Image.open('smyu24.png') as file:
        draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)
        file.save('smyu24.png')


lines()