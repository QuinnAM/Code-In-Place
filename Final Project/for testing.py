from simpleimage import SimpleImage
from PIL import Image, ImageTk
import random
import tkinter

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

COLS = 8
ROWS = 4


def main():


    random_pair = random.choice(list(IMAGE_LOCATION.items()))
    image_path = random_pair[1]
    mosaic = make_mosaic(image_path)


    canvas = make_canvas(mosaic.width, mosaic.height, "Woohoo!")

    background = ImageTk.PhotoImage(mosaic)

    canvas.create_image(0,0, image=background, anchor = "nw")

    results_message = "you are less fat!"  "\nCongratulations!"


    canvas.create_text(700, 360, fill = "black", anchor = "center", font = "times 100 bold", text = results_message)


    tkinter.mainloop()


def make_mosaic(image_path):

    image = Image.open(image_path)

    image_resized = calculate_size(image, MAX_WIDTH, MAX_HEIGHT)

    width, height = image_resized.size

    background = Image.new("RGB", ((width * 8), (height * 4)), (255, 255, 255))


    for x in range(COLS):
        for y in range (ROWS):



            bg_random = choose_bg_col()

            patch_bg = Image.new("RGB", (width, height), (bg_random[0], bg_random[1], bg_random[2]))
            patch_bg.paste(image_resized, (0, 0), image_resized)

            place_patch(background, patch_bg, x*width, y*height)


    return background


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












def make_canvas(width, height, title):
    """
    Creates a background for the congratulations image
    """
    window = tkinter.Tk()
    window.minsize(width=width, height=height)
    window.title(title)
    background = tkinter.Canvas(window, width=width, height=height, bg='black')
    background.pack(expand="yes", fill="both")
    return background





















if __name__ == '__main__':
    main()