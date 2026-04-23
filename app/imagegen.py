from PIL import Image, ImageDraw
from simpilfont import SimPILFont
import numpy as np
import colorsys


def generate_background(hue, width, height):
    a = np.zeros((width, height, 3), dtype=np.uint8)
    rgb = colorsys.hsv_to_rgb(hue, 0.4, 0.7)
    for i in range(3):
        a[:, :, i].fill(rgb[i] * 255)
    return Image.fromarray(a)


def generate_scorecard(rgb: str, topic: str, score: str):
    # Generate background
    rgb = [int(float(d)) for d in rgb.split(" ")]
    array = np.zeros((400, 500, 3), dtype=np.uint8)
    for i in range(3):
        array[:, :, i].fill(rgb[i])
    img = Image.fromarray(array)
    draw = ImageDraw.Draw(img)

    # Sort out fonts
    sf = SimPILFont('app/static/fonts/vremena-grotesk', 'app/static/fonts/Peppa Pig-FontZillion')
    sf.export()
    topic_font = sf('VremenaGrotesk 64 bold').font
    score_font = sf('PeppaPig 32').font


    # Score text
    draw.text((250,100), f"you got {score}/7", (0,0,0), font=score_font, align="center", anchor="ms")

    # Topic text
    draw.text((250,200), topic.upper(), (0,0,0), font=topic_font, align="center", anchor="ms")

    return img
    

if __name__ == "__main__":
    img = generate_scorecard("167.57999999999996 178.5 107.1", "Fruit", "5")
    img.show()