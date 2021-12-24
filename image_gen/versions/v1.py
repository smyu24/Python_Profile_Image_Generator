import numpy as np
from PIL import Image
import os
from random import seed
from random import randint

dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480


# using ETH block number as starting random number seed
b=11981207
seed(b)

#head color - randomly generate each number in an RGB color
hd = (randint(0, 256), randint(0, 256), randint(0, 256))
c=randint(0,500)
seed(c)

#throat color - same as head color
th = (randint(0, 256), randint(0, 256), randint(0, 256))
d = randint(0,1000)
seed(d)

#eye "white" color
# if random number between 1-1000 is 47 or less - Crazy Eyes!
if d > 47:
    # normal eyes are always the same color
    ew = (240,248,255)
    ey = (0, 0, 0)
else:
    # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
    ew = (randint(0, 256), randint(0, 256), randint(0, 256))
    ey = (154, 0, 0)
e = randint(0,1000)
seed(e)

# beak color
f = randint(0, 1000)
if f > 500:
    # if random number is 501-1000 >> grey beak
    bk = (152, 152, 152)
elif 500 >= f > 47:
    # 48-500 >> gold beak
    bk = (204, 172, 0)
elif 47 >= f > 7:
    # 8 >> 47 >> red beak
    bk = (204, 0, 0)
else:
    # random number is 7 or less >> black beak
    bk = (0, 0, 0)

# background color
bg = (238, 238, 238)
# outline color
ol = (0, 0, 0)

basic_bird = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, th, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, th, th, th, th, th, ol, bg, bg, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

woodpecker = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, bk, bk, bk, ol, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, ol, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, th, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, th, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

jay = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, th, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, th, th, th, th, th, ol, bg, bg, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

eagle = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

cockatoo = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, ol, ol, th, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, bg, ol, th, ol, bg, ol, th, th, ol, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, ol, bg, ol, th, ol, ol, ol, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, th, ol, bg, ol, th, th, th, ol, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, th, th, ol, ol, ol, th, th, ol, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, ol, th, th, th, ol, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, ol, th, th, th, hd, hd, hd, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, ol, ol, ol, ol, th, th, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, ol, th, th, th, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, th, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, ol, ol, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, bg, bg, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

# choose which bird image to use
seed(f)
g = randint(0,1000)
if g > 250:
    # if random number is 251 - 1000 >> basic bird
    pixels = basic_bird
    p = "basic"
elif 250 >= g > 100:
    # 101 - 250 >> jay
    pixels = jay
    p = "jay"
elif 100 >= g > 40:
    # 41 - 100 >> woodpecker
    pixels = woodpecker
    p = "pecker"
elif 40 >= g > 5:
    # 6 - 40 >> eagle
    pixels = eagle
    p = "eagle"
else:
    # if random number is 5 or less >> cockatoo!!
    pixels = cockatoo
    p = "cockatoo"

# convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

username = "smyu24"

# use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image = new_image.resize(dimensions, resample=0)
imgname = fr'{dirname}/profile_images/{str(username)}.png'
print(imgname)
new_image.save(imgname)

"""
with open('readme.txt', 'x') as f:
    f.write('Create a new text file!')

from PIL import Image
with Image.open("hopper.jpg") as im:
    im.rotate(45).show()

    f= open("guru99.txt","w+")
"""
#https://newbedev.com/100x100-image-with-random-pixel-colour


"""
    You can convert to a string like this:

import base64

with open("image.png", "rb") as image:
    b64string = base64.b64encode(image.read())
That should give you the same results as if you run this in Terminal:

base64 < image.png
And you can convert that string back to a PIL Image like this:

from PIL import Image
import io

f = io.BytesIO(base64.b64decode(b64string))
pilimage = Image.open(f)
"""

"""
    https://stackoverflow.com/questions/54147694/python-how-to-turn-an-image-into-a-string-and-back
    https://www.geeksforgeeks.org/python-convert-image-to-string-and-vice-versa/
"""