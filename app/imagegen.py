from PIL import Image
import numpy as np
import colorsys





def generate_background(hue, width, height):
    a = np.zeros((width, height, 3), dtype=np.uint8)
    rgb = colorsys.hsv_to_rgb(hue, 0.4, 0.7)
    for i in range(3):
        a[:,:,i].fill(rgb[i] * 255)
    return Image.fromarray(a)


