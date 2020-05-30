from PIL import Image, ImageTk
import random
import tkinter
import time
import math

WEIGHT_DICT = {"sugar glider":
                { "weight" : 0.1,
                "location" :"D:/UserFiles/Desktop/Code In Place/Final Project/images/sugar.png"},
               "hedgehog":
                { "weight" : 0.8,
                "location" : "D:/UserFiles/Desktop/Code In Place/Final Project/images/hedgehog.png" },
               "watermelon":
                { "weight" : 0.02,
                 "location" : "D:/UserFiles/Desktop/Code In Place/Final Project/images/watermelon.png"},
               "lego minifig":
                { "weight" : 0.0029,
                 "location" : "D:/UserFiles/Desktop/Code In Place/Final Project/images/minifig.png"}}


BG_COLOR =  {"Pink" : (255, 0, 127), "Turquoise" : (0, 255, 255), "Purple" : (127,0,255), "Yellow" : (255,255,0),
             "Green": (15,207,8), "Orange": (255,108,10), "Blue":(8,0,242)}

WIDTH = 1280
LENGTH = 720

MAX_WIDTH = 150
MAX_HEIGHT = 160

COLS = 8
ROWS = 4

BANNER_HEIGHT = 50
BANNER_WIDTH = 400
def main():

    name = str(input("Please enter your name: "))

    orig_weight = float(input("Please enter your start weight: "))
    new_weight = float(input("Please enter your current weight: "))
    goal_weight = float(input("Please enter your goal weight: "))
    lost_weight = (orig_weight - new_weight)
    to_lose = (new_weight - goal_weight)

    with open("D:/UserFiles/Desktop/Code In Place/Final Project/profiles/" + name + ".txt", "a") as file:
        file.write(str(orig_weight) + "\n" + str(new_weight) + "\n")
    with open("D:/UserFiles/Desktop/Code In Place/Final Project/profiles/" + name + "_goal" + ".txt", "a") as file:
        file.write(str(goal_weight))

    random_unit = choose_random_unit()

    units_to_lose = to_lose / random_unit[1]["weight"]



    unit_weight = lost_weight / random_unit[1]["weight"]

    congrats_message = print_congratulations_message(lost_weight)
    results_message = print_weight_in_units(unit_weight, random_unit)



    image_path = random_unit[1]["location"]
    mosaic = make_mosaic(image_path)

    width = mosaic.width
    height = mosaic.height


    canvas = make_canvas(mosaic.width, mosaic.height, "Woohoo!")


    background = ImageTk.PhotoImage(mosaic)

    canvas.create_image(0,0, image=background, anchor = "nw")



    canvas.create_text((width / 2), 150, fill = "black", anchor = "center", font = "times 50 bold",
                       text = congrats_message +
                       "\n" + results_message)





    banner, text = make_banner(canvas, random_unit[0], units_to_lose)


    # animation loop
    while canvas.coords(banner)[0] < width :
        # update the world
        canvas.move(banner, 1, 0)
        canvas.move(text, 1, 0)

        canvas.update()

        # pause
        time.sleep(1/50.) #parameter is seconds to pause.




    tkinter.mainloop()

    ## record weight
    ## record new weight
    ## compare two values
    ## print gain or loss of weight
    ##make list of animals
    ## comppare to lists

    ## print out congratulations on an image made of the animal you have lost

    ## ask for goal weight
    ## kilos, pounds and stone
    ## ask user what their favourite colour is and colour all image backgrounds to that colour
    ## message for gaining weight
    ## BMI checker
    ## graph of progression
    ## tell weight difference between beginning and last weigh in
    ## calorie amount needed for goal weight by certain date
    ## reasonable or not - give message
    ## make it so they can add their own animals in


def read_list(name):
    mylist = []
    with open ("D:/UserFiles/Desktop/Code In Place/Final Project/profiles/" + name + ".txt", "r") as file:
        for line in file:
            line = float(line.strip())
            mylist.append(line)

    return mylist

def choose_random_unit():
    random_unit = random.choice(list(WEIGHT_DICT.items()))
    return random_unit

def print_congratulations_message(lost_weight):

    if lost_weight == 1:
        results = ("Congratulations! You have lost " + str(int(lost_weight)) + " kilo!")
    elif (lost_weight % 1 != 0):
        results = ("Congratulations! You have lost " + str(lost_weight) + " kilos!")
    elif (lost_weight % 1 == 0):
        results = ("Congratulations! You have lost " + str(int(lost_weight)) + " kilos!")

    return results

def print_weight_in_units(unit_weight, random_unit):

    if unit_weight == 1:
        results = ("That is " + str(int(unit_weight)) + " " + random_unit[0] + "!")
    elif (unit_weight % 1 != 0):
        results = ("That is " + str(unit_weight) + " " + random_unit[0] + "s!")
    elif (unit_weight % 1 == 0):
        results = ("That is " + str(int(unit_weight)) + " " + random_unit[0] + "s!")
    return results


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

def make_banner(canvas, random_unit,units_to_lose):


    banner_text = canvas.create_text(0, 550, fill="blue", anchor="w", font="times 30 bold", text="Just " +
                                str(int(units_to_lose)) + " " + random_unit + "s to lose!")
    text_size = (canvas.bbox(banner_text))

    canvas.move(banner_text, -text_size[2], 0)

    text_size = (canvas.bbox(banner_text))

    banner = canvas.create_rectangle(text_size[0] - 20, text_size[1] - 20, text_size[2] + 20, text_size[3] + 20,
                                     fill="white")

    canvas.tag_raise(banner_text)

    return banner, banner_text






if __name__ == '__main__':
    main()


