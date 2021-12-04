zones = []
ip = []
words = []
import soco
from soco import SoCo
import PIL
from PIL import Image, ImageTk
import time
from tkinter import *
from tkinter import font
from urllib.request import urlopen
import random
import io
global volume
volume = 0
def callback():

    title = "New Title"
    
    my_picture = "sonos.jpg"
    image = PIL.Image.open(my_picture)
    pil_img = image.resize((220, 220))
    tk_img = ImageTk.PhotoImage(pil_img)
    panel.configure(image=tk_img)
    panel.image = tk_img

    artist = "Artist: " + "New Artist"
    Label3.configure(text = artist)
    Label1.configure(text = title)
    Label2.configure(text = str(volume) + "% Volume")

def volup():
    volume = volume + 1
    Label2.configure(text = str(volume) + "% Volume")

def voldown():
    volume = volume - 1
    Label2.configure(text = str(volume) + "% Volume")

root = Tk()
root.title("Sonos Controller | In " + "A Room")
root.configure(background='black')


root.iconbitmap('photo.ico')

title = "Title"
artist = "Artist: " + "artist"
volume = str(2) + "% Volume"

#
#Album Art

my_picture = "sonos.jpg"

    
image = PIL.Image.open(my_picture)
pil_img = image.resize((200, 200))
tk_img = ImageTk.PhotoImage(pil_img)
#
panel = Label(root, bg="purple", image=tk_img)
panel.grid(row=3, column=0, sticky=W)
panel.configure(image=tk_img)
panel.image = tk_img

#Labels and Buttons

#Title
Label1 = Label(root, fg="white", bg="black", font=("Noto Serif", 15), text = title)
Label1.grid(row=0, column=0, sticky=W)
f = font.Font(Label1, Label1.cget("font"))
f.configure(underline = True)
Label1.configure(font=f)

#Volume
Label2 = Label(root, fg="white",bg="black", font=("Noto Serif", 12), text = volume)
Label2.grid(row=0, column=2, sticky=W)

#Artist
Label3 = Label(root, fg="white",bg="black", font=("Noto Serif", 10), text = artist)
Label3.grid(row=1, column=0, sticky=W)


playimg=PhotoImage(file="play.png")
volupimg=PhotoImage(file="volup.png")
voldownimg=PhotoImage(file="voldown.png")
Button1 = Button(root, bg = "black",border = "0", image=playimg,command=callback, height = 70, width = 70).grid(row=3, column=1, sticky=W)
Button(root, bg = "purple",border= "0", image = volupimg,command=callback).grid(row=0, column=1, sticky=W)
Button(root, bg = "purple",border= "0", image = voldownimg,command=callback).grid(row=1, column=1, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="   Next   ",command=callback).grid(row=2, column=2, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10),text="Previous",command=callback).grid(row=2, column=1, sticky=W)

Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="Unmute",command=callback).grid(row=2, column=3, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="mute",command=callback).grid(row=2, column=4, sticky=W)

root.mainloop()





