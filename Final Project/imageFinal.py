from simpleimage import SimpleImage
from PIL import Image
import random

WIDTH = 1280
LENGTH = 720

IMAGE_LOCATION = {"sugar glider" : "D:/UserFiles/Desktop/Code In Place/Final Project/images/sugar.png",
               "hedgehog" : "D:/UserFiles/Desktop/Code In Place/Final Project/images/hedgehog.png" ,
               "teaspoon" : "D:/UserFiles/Desktop/Code In Place/Final Project/images/teaspoon.png",
               "minifig" : "D:/UserFiles/Desktop/Code In Place/Final Project/images/minifig.png"}

BG_COLOR =  {"Pink" : (255, 0, 127), "Turquoise" : (0, 255, 255), "Purple" : (127,0,255), "Yellow" : (255,255,0),
             "Green": (15,207,8), "Orange": (255,108,10), "Blue":(8,0,242)}

##sugar = 300, 200
##hedgehog = 300, 200
##teaspoon = 300, 200
##egg = 300, 150

MAX_WIDTH = 150
MAX_HEIGHT = 160

COLS = 10
ROWS = 5


def main():





    random_pair = random.choice(list(IMAGE_LOCATION.items()))
    image_path = random_pair[1]
    image = Image.open(image_path)

    image_resized = calculate_size(image, MAX_WIDTH, MAX_HEIGHT)

    width, height = image_resized.size



    background = Image.new("RGB", ((width * 10), (height * 5)), (255, 255, 255))

    """    patch_bg = Image.new("RGB", (width, height), (bg_random[0], bg_random[1], bg_random[2]))"""



    for x in range(COLS):
        for y in range (ROWS):

            bg_random = choose_bg_col()

            patch_bg = Image.new("RGB", (width, height), (bg_random[0], bg_random[1], bg_random[2]))
            patch_bg.paste(image_resized, (0, 0), image_resized)

            place_patch(background, patch_bg, x*width, y*height)

    background.show()


def choose_bg_col():
    bg_color = random.choice(list(BG_COLOR.items()))[1]
    return bg_color






def place_patch(background, patch_bg, x_position, y_position):
    for x in range(patch_bg.width):
        for y in range(patch_bg.height):
            pixel = patch_bg.getpixel((x,y))
            background.putpixel((x_position+x, y_position+y), pixel)











def calculate_size (image, MAX_WIDTH, MAX_HEIGHT):
    width, height = image.size

    ratio = width / height
    if width <= height:
        resized_image = image.resize((MAX_HEIGHT, int(MAX_HEIGHT / ratio)))
    else: resized_image = image.resize((int(MAX_WIDTH * ratio), MAX_WIDTH))

    return resized_image





    """def calculate_ratio(image):

    if image == "sugar glider" or "teaspoon" or "hedgehog":
        image_resized = image.resize ((300, 200))
    else: image_resized = image.resize ((250, 320))
    return image_resizedZ
    """




    """
    for x in range (image.width):
        for y in range (image.height):
            pixel = image.get_pixel(x, y)
            background.set_pixel(x, y, pixel)
    background.show()
    """
    """    for x in range(100):
        for y in range (100):
        pixel = get.pixel(x, y)
        set.pixel (x, y)

    background.show()"""










if __name__ == '__main__':
    main()