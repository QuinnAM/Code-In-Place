from PIL import Image, ImageTk
import random
import tkinter
import time


"""This program will take some input from the user.  A name, current weight, a start weight and a goal weight, and it 
will create a text file where it will save this information under the name provided.
The program will then calculate these weights in other random units, provided in a dictionary. It will create a 
mosaic of the unit and show this mosaic along with a scrolling bar containing how many of the units are left 
to lose before goal weight."""


# This is the dictionary containing the units.
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

# This is the dictionary containing the colours that will make up the mosaic backgrounds.
BG_COLOR =  {"Pink" : (255,20,147) , "Turquoise" : (0, 255, 255), "Purple" : (127,0,255), "Yellow" : (255,255,0),
             "Green": (15,207,8), "Orange": (255,108,10),  "Blue":(8,0,242)}


WIDTH = 1280
LENGTH = 720

MAX_WIDTH = 150
MAX_HEIGHT = 160

COLS = 8
ROWS = 4

BANNER_HEIGHT = 50
BANNER_WIDTH = 400


def main():


    #This section asks for user input.
    name = str(input("Please enter your name: "))
    orig_weight = float(input("Please enter your start weight: "))
    new_weight = float(input("Please enter your current weight: "))
    goal_weight = float(input("Please enter your goal weight: "))

    #This section does the necessary calculations.
    lost_weight = (orig_weight - new_weight)
    to_lose = (new_weight - goal_weight)

    #This section writes the information to two files, one for the rolling new weights and one for the goal.
    with open("D:/UserFiles/Desktop/Code In Place/Final Project/profiles/" + name + ".txt", "a") as file:
        file.write(str(orig_weight) + "\n" + str(new_weight) + "\n")
    with open("D:/UserFiles/Desktop/Code In Place/Final Project/profiles/" + name + "_goal" + ".txt", "a") as file:
        file.write(str(goal_weight))

    #This finds which unit the program will be using for comparison.
    random_unit = choose_random_unit()

    #These are some necessary calculations for use in the graphics display.
    units_to_lose = to_lose / random_unit[1]["weight"]
    unit_weight = lost_weight / random_unit[1]["weight"]

    #This prints the final messages.
    congrats_message = print_congratulations_message(lost_weight)
    results_message = print_weight_in_units(unit_weight, random_unit)

    #This indicates the location of the image to be used in the mosaic.
    image_path = random_unit[1]["location"]
    mosaic = make_mosaic(image_path)

    #This gives the width and height of the final mosaic.  Although the height was not used in future functions.
    # I thought it might be useful for future developments.
    width = mosaic.width
    height = mosaic.height

    #This creates a canvas the size and width of the mosaic.
    canvas = make_canvas(mosaic.width, mosaic.height, "Woohoo!")

    #This turns the mosaic into an image that can be used by Tkinter on a canvas, and renames it 'background'.
    background = ImageTk.PhotoImage(mosaic)

    #This section puts together the two final messages on top of the background.
    canvas.create_image(0,0, image=background, anchor = "nw")


    #This section creates a background for the congratulations and results message.
    msg =  canvas.create_text((width / 2), 150, fill = "light sky blue", anchor = "center", font = "times 50 bold",
                       text = congrats_message + "\n" + results_message)
    message_bg = congrats_backgrounds(canvas, msg)

    #This calls a function that makes a banner and the text to go on top of it.
    banner, text = make_banner(canvas, random_unit[0], units_to_lose)


    #This runs an animation loop over my banner.
    while canvas.coords(banner)[0] < width :

        canvas.move(banner, 1, 0)
        canvas.move(text, 1, 0)

        canvas.update()


        time.sleep(1/50.) #parameter is seconds to pause.



    #This keeps my final product from closing.
    tkinter.mainloop()


#This function randomises the choice of unit to be used throughout the program.
def choose_random_unit():
    random_unit = random.choice(list(WEIGHT_DICT.items()))
    return random_unit


#This function creates a background for the congratulations and results message.
def congrats_backgrounds(canvas, text):

    congrats_size = (canvas.bbox(text))

    congrats_background = canvas.create_rectangle(congrats_size[0] - 20, congrats_size[1] - 20, congrats_size[2] + 20,
                                                  congrats_size[3] + 20,
                                                  fill="dark green")

    canvas.tag_raise(text)


    return congrats_background

#This function returns a constructed congratulations message.  It calculates if the weight lost should be plural or
#singular digits and returns it in the correct form.
def print_congratulations_message(lost_weight):

    if lost_weight == 1:
        results = ("Congratulations! You have lost " + str(int(lost_weight)) + " kilo!")
    elif (lost_weight % 1 != 0):
        results = ("Congratulations! You have lost " + str(lost_weight) + " kilos!")
    elif (lost_weight % 1 == 0):
        results = ("Congratulations! You have lost " + str(int(lost_weight)) + " kilos!")

    return results


#This function takes the unit weight, and  with the correct grammar depending on if the user has lost 1 or greater than
# 1 of the units.
def print_weight_in_units(unit_weight, random_unit):

    if unit_weight == 1:
        results = ("That is " + str(int(unit_weight)) + " " + random_unit[0] + "!")
    elif (unit_weight % 1 != 0):
        results = ("That is " + str(unit_weight) + " " + random_unit[0] + "s!")
    elif (unit_weight % 1 == 0):
        results = ("That is " + str(int(unit_weight)) + " " + random_unit[0] + "s!")
    return results


#This function takes the image path from the dictionary and creates a mosaic with the background colour randomised,
#based on the colour chosen by another function.
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

#This function chooses the colour of the mosaic piece background.
def choose_bg_col():
    bg_color = random.choice(list(BG_COLOR.items()))[1]
    return bg_color

#This function places the patch on the plain background.
def place_patch(background, patch_bg, x_position, y_position):
    for x in range(patch_bg.width):
        for y in range(patch_bg.height):
            pixel = patch_bg.getpixel((x,y))
            background.putpixel((x_position+x, y_position+y), pixel)

#This function calculates the size of the mosaic based on the MAX_HEIGHT and MAX_WIDTH in the constants, so that the
#end result is not too big to fit on any screen.
def calculate_size (image, MAX_WIDTH, MAX_HEIGHT):
    width, height = image.size

    ratio = width / height
    if width <= height:
        resized_image = image.resize((MAX_HEIGHT, int(MAX_HEIGHT / ratio)))
    else: resized_image = image.resize((int(MAX_WIDTH * ratio), MAX_WIDTH))

    return resized_image

#This function creates the base canvas for the whole final product.
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


#This function creates and places a banner containing text off the left side of the screen, to be moved slowly across.
def make_banner(canvas, random_unit,units_to_lose):


    banner_text = canvas.create_text(0, 550, fill="lawn green", anchor="w", font="times 30 bold", text="Just " +
                                str(int(units_to_lose)) + " " + random_unit + "s to lose!")
    text_size = (canvas.bbox(banner_text))

    canvas.move(banner_text, -text_size[2], 0)

    text_size = (canvas.bbox(banner_text))

    banner = canvas.create_rectangle(text_size[0] - 20, text_size[1] - 20, text_size[2] + 20, text_size[3] + 20,
                                     fill="dark green")

    canvas.tag_raise(banner_text)

    return banner, banner_text






if __name__ == '__main__':
    main()


