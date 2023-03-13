import colorgram


rgb_colors = []
colors = colorgram.extract('/home/acer/z notes/python/color Identifier/images.png',5)
import random

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)


print(rgb_colors)
