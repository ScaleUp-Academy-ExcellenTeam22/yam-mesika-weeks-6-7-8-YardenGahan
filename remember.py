"""
Requieremenrs : PIL Package

This program gets path to a file, then is takes the row number of each black pixel,
then uses the chr() function to convert it to a letter.
@param : path - path to a png file
@return : string
"""

from PIL import Image


def decode_png(path):
    img = Image.open(path).convert('RGB')
    pixel = img.load()

    width = img.size[0]
    height = img.size[1]

    message = ""
    for i in range(width):
        for j in range(height):
            if pixel[i, j] == (255, 255, 255):  # if pixel is white
                pass
            else:  # if pixel is black
                message += chr(j)
    print(message)


decode_png('code.png')
