from simpleimage import SimpleImage
from PIL import Image, ImageTk
import random
from tkinter import *

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


    # create the canvas, size in pixels
    canvas = Canvas(width=300, height=200, bg='black')

    # pack the canvas into a frame/form
    canvas.pack(expand=YES, fill=BOTH)

    # load the .gif image file
    gif1 = PhotoImage(file='D:/UserFiles/Desktop/Code In Place/Final Project/images/minifig.png')

    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
    canvas.create_image(50, 10, image=gif1, anchor=NW)

    # run it ...
    mainloop()


if __name__ == '__main__':
    main()