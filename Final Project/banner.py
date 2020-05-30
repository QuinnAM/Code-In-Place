from PIL import Image, ImageTk
import tkinter
import time
import random
import math

def main():


    canvas = make_canvas(720, 720, "stuff")

    banner_size = 100


    banner = canvas.create_rectangle(0, 350, banner_size, 40, fill = "white")
    text = canvas.create_text(60, 250, fill="red", anchor="center", font="times 30 bold", text="Just ")



    # animation loop
    while canvas.coords(banner)[0] < 800 :
        # update the world
        canvas.move(banner, 1, 0)
        canvas.move(text, 1, 0)

        canvas.update()

        # pause
        time.sleep(1/50.) #parameter is seconds to pause.

    tkinter.mainloop()










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

