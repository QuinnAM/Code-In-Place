from PIL import ImageTk
from simpleimage import SimpleImage
import random
import tkinter

WIDTH = 1280
HEIGHT = 720

def main():


    background = make_canvas(WIDTH, HEIGHT, "Congratulations!")

    background.create_text(700, 360, anchor="w", font="times", text="Congratulations!")

    background.mainloop()


def make_canvas(width, height, title):
    """
    Creates a background for the congratulations image
    """
    window = tkinter.Tk()
    window.minsize(width=width, height=height)
    window.title(title)
    background = tkinter.Canvas(window, width=width + 1, height=height + 1)
    background.pack()
    return background

    """    background = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
    background.show()"""







if __name__ == '__main__':
    main()