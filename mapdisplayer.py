import sys, glob
import subprocess
import tkinter, random
from PIL import Image, ImageTk

cities = glob.glob("./citymaps/*/")

def showPIL(pilImage):
    imgWidth, imgHeight = pilImage.size
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
import os, sys
import Tkinter
import Image, ImageTk

def button_click_exit_mainloop (event):
        event.widget.quit() # this will cause mainloop to unblock.

        root = Tkinter.Tk()
        root.bind("<Button>", button_click_exit_mainloop)
        root.geometry('+%d+%d' % (100,100))
        dirlist = os.listdir('.')
        old_label_image = None
        for f in dirlist:
                try:
                            image1 = Image.open(f)
                                    root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
                                            tkpi = ImageTk.PhotoImage(image1)
                                                    label_image = Tkinter.Label(root, image=tkpi)
                                                            label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])
                                                                    root.title(f)
                                                                            if old_label_image is not None:
                                                                                            old_label_image.destroy()
                                                                                                    old_label_image = label_image
                                                                                                            root.mainloop() # wait until user clicks the window
                                                                                                                except Exception, e:
                                                                                                                            # This is used to skip anything not an image.
                                                                                                                                    # Warning, this will hide other errors as well.
mport os, sys
import Tkinter
import Image, ImageTk

def button_click_exit_mainloop (event):
        event.widget.quit() # this will cause mainloop to unblock.
import os, sys
import Tkinter
import Image, ImageTk

def button_click_exit_mainloop (event):
        event.widget.quit() # this will cause mainloop to unblock.

        root = Tkinter.Tk()
        root.bind("<Button>", button_click_exit_mainloop)
        root.geometry('+%d+%d' % (100,100))
        dirlist = os.listdir('.')
        old_label_image = None
        for f in dirlist:
                try:
                            image1 = Image.open(f)
                                    root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
                                            tkpi = ImageTk.PhotoImage(image1)
                                                    label_image = Tkinter.Label(root, image=tkpi)
                                                            label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])
                                                                    root.title(f)
                                                                            if old_label_image is not None:
                                                                                            old_label_image.destroy()
                                                                                                    old_label_image = label_image
                                                                                                            root.mainloop() # wait until user clicks the window
                                                                                                                except Exception, e:
                                                                                                                            # This is used to skip anything not an image.
                                                                                                                                    # Warning, this will hide other errors as well.
                                                                                                                                            pass
        root = Tkinter.Tk()
        root.bind("<Button>", button_click_exit_mainloop)
        root.geometry('+%d+%d' % (100,100))
        dirlist = os.listdir('.')
        old_label_image = None
        for f in dirlist:
                try:
                            image1 = Image.open(f)
                                    root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
                                            tkpi = ImageTk.PhotoImage(image1)
                                                    label_image = Tkinter.Label(root, image=tkpi)
                                                            label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])
                                                                    root.title(f)
                                                                            if old_label_image is not None:
                                                                                            old_label_image.destroy()
                                                                                                    old_label_image = label_image
                                                                                                            root.mainloop() # wait until user clicks the window
                                                                                                                except Exception, e:
                                                                                                                            # This is used to skip anything not an image.
                                                                                                                                    # Warning, this will hide other errors as well.
                                                                                                                                            passpass
while True:dd
    city = random.choice(cities)
    bashCommand = "feh "+city+"1.jpg"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("showing")
    time.sleep(5)
    image = Image.open(city+"2.jpg")
    showPIL(image)
    time.sleep(5)
    image = Image.open(city+"3.jpg")
    showPIL(image)
    time.sleep(5)
    image = Image.open(city+"6.jpg")
    showPIL(image)
    time.sleep(5)
    root.mainloop()


