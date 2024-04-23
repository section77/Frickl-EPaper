#!/usr/bin/env python3

from PIL import Image
import json

'''
imgconvert.py

This script reads a GIF file and outputs a C header file in which the layers are defined as 
char arrays.
'''

directory = 'data/'
filename = directory + 'Test.gif'

im = Image.open(filename)

layer = 0
pixelbuf = []  # type: ignore[var-annotated]


def setPixel(buf, x, y):
    buf[x][y // 8] &= (0xff ^ 0x80 >> (y % 8))


def mirror(text):
    return text[::-1]


while (True):
    try:
        im.seek(layer)
    except EOFError:
        break

    (mx, my) = im.size
    #print(f"Layer {layer}: {mx}, {my}")

    # an empty image has all bits set to 1
    pixelbuf.append([[255 for y in range(my // 8)] for x in range(mx)])

    img = im.convert("RGB")
    for x in range(mx):
        for y in range(my):
            px = img.getpixel((x, y))
            if (px != (255, 255, 255)):
                # print(f"x: {x}, y:{y}, {px}")
                setPixel(pixelbuf[layer], x, y)

    #img.save(directory + f'Testerle{layer}.bmp')
    layer += 1

layer = 0
for l in pixelbuf:
    print(f"const char image{layer}[{mx}][{my//8}] = {{")
    for x in l:
        print("\t{", end='')
        #for b in x:
        #    print(f'{b}', end=',')
        print(','.join(map(str,x)), end='')
        print("},")
    print("};")
    layer += 1