from PIL import Image, ImageDraw, ImageFont
# from simpilfont import SimPILFont
import colorsys
import os

basedir = os.path.dirname(os.path.abspath(__file__))

print(basedir)



def generate_scorecard(rgb: str, topic: str, score: str):
    # Generate background
    rgb = tuple(int(float(d)) for d in rgb.split(" "))
    img = Image.new('RGB', (500, 400), rgb)
    draw = ImageDraw.Draw(img)

    # Sort out fonts
    base_folder = basedir.replace("\\", "/")
    print(base_folder + "/static/fonts/vremena-grotesk/Vremena.ttf")
    topic_font = ImageFont.truetype(base_folder + "/static/fonts/vremena-grotesk/Vremena.ttf", 64)
    score_font = ImageFont.truetype(base_folder + "/static/fonts/Peppa Pig-FontZillion/peppa pig.ttf", 32)
    # sf = SimPILFont(os.path.join(basedir, 'static/fonts/vremena-grotesk') + '/', 
    #                 os.path.join(basedir, 'static/fonts/Peppa Pig-FontZillion') + '/')
    # topic_font = sf('VremenaGrotesk 64 bold').font
    # score_font = sf('PeppaPig 32').font
    # sf.export()

    # Score text
    draw.text((250,100), f"you got {score}/7", (0,0,0), font=score_font, align="center", anchor="ms")

    # Topic text
    topic_text = topic.upper()
    if len(topic_text) > 10:
        print(topic_text)
        if " " in topic_text:
            topic_text = topic_text.replace(" ", "\n")
        for word in topic_text.split("\n"):
            if len(word) > 10:
                topic_font = ImageFont.truetype(base_folder + "/static/fonts/vremena-grotesk/Vremena.ttf", 48)
    draw.text((250,200), topic_text, (0,0,0), font=topic_font, align="center", anchor="ms")

    return img
    

if __name__ == "__main__":
    img = generate_scorecard("167.57999999999996 178.5 107.1", "Fruit", "5")
    img.show()