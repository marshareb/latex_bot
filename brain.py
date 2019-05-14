import BotMe.main as Bot
import time
import os
from pdf2image import convert_from_path
from PIL import Image

default_coordinates = (1000, 0, 3000, 800)

def crop(image_path, coords, saved_location):
    # https://www.blog.pythonlibrary.org/2017/10/03/how-to-crop-a-photo-with-python/
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)

def process_message(message):
    message = message.split()

    try:
        print(message[0])
    except:
        return None
    if message[0].lower() == '!coord':
        default_coordinates = tuple(' '.join(message[1:]))
    elif message[0].lower() == '!latex':
        message = ' '.join(message[1:])
        f = open('test.tex', 'w')
        f.write(
            r"\documentclass[10pt,a4paper]{article}" +
            r" \usepackage[utf8]{inputenc}" +
            r" \usepackage{amsmath}" +
            r" \usepackage{amsfonts}" +
            r" \usepackage{amssymb}" +
            r" \pdfpageheight=2in" +
            r" \pdfpagewidth=8.5in" +
            r" \addtolength{\topmargin}{-1.25in}" +
            r" \begin{document}" +
            r" \[" + str(message) + r"\] " +
                                  r" \end{document}")
        f.close()
        os.system("pdflatex test.tex")
        pages = convert_from_path('test.pdf', 500)
        for page in pages:
            page.save('test.png', 'PNG')
        crop('test.png', default_coordinates, 'test2.png')
        return 'test2.png'

    return None


if __name__ == '__main__':    
    bot = Bot.Manager('')
    bot.create_bot('latexbot', 'Test')
    # Loop to continuously run
    while True:
        x = process_message(bot.retrieve_message()[1])
        if x != None:
            bot.post_picture('test.png')
time.sleep(3)

