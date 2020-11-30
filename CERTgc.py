

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

TEXT_Y_PIXEL = 830
TEXT_SIZE = 50
TEMPLATE_IMG = "/content/certgen2/template.png"
name = input('Please provide your registered name: ')
FONT_TTF_FILE = "/content/certgen2/Montserrat-Light.otf"

def output_cert(name):
    img = Image.open(TEMPLATE_IMG)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(FONT_TTF_FILE, TEXT_SIZE)
    # draw.text((x, y),"Sample Text",(r,g,b))
    img_width, img_height = img.size
    text_width, text_height = font.getsize(name.title())

    draw.text((img_width/2 - text_width/2, TEXT_Y_PIXEL),
              name.title(), (0, 0, 0), font=font)
    img.save(f'{name}.png')
    print('Certificate has been successfully generated for', name)

output_cert(name)

# if __name__ == "__main__":
#     os.makedirs('output', exist_ok=True)
#     names = []
#     with open(NAME_LIST_TXT, 'r') as f:
#         names = f.readlines()

#     for name in names:
#         name = name.replace("\n", "").replace("/", "")
#         output_cert(name)