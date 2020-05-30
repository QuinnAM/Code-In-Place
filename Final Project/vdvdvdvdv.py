import tempfile, os

from pyx import *
import Tkinter
import Image, ImageTk

# first we create some pyx graphics
c = canvas.canvas()
c.text(0, 0, "Hello, world!")
c.stroke(path.line(0, 0, 2, 0))

# now we use pipeGS (ghostscript) to create a bitmap graphics
fd, fname = tempfile.mkstemp()
f = os.fdopen(fd, "wb")
f.close()
c.pipeGS(fname, device="pngalpha", resolution=100)
# and load with PIL
i = Image.open(fname)
i.load()
# now we can already remove the temporary file
os.unlink(fname)

# finally we can use this image in Tkinter
root = Tkinter.Tk()
root.geometry('%dx%d' % (i.size[0],i.size[1]))
tkpi = ImageTk.PhotoImage(i)
label_image = Tkinter.Label(root, image=tkpi)
label_image.place(x=0,y=0,width=i.size[0],height=i.size[1])
root.mainloop()