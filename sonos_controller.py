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
import io

global room
global zone


#Speaker IP Address
room = SoCo("192.168.1.41")

def kitchen():
    global room
    global zone
    zone = kitchen
    room = SoCo("192.168.1.43")
    root.title("Sonos Controller | In " + "Kitchen")
    callback()
    
def bedroom():
    global room
    global zone
    zone = bedroom
    room = SoCo("192.168.1.41")
    root.title("Sonos Controller | In " + "Olly's Bedroom")
    callback()
    
def play():
    if room.get_current_transport_info().get('current_transport_state') == "PLAYING":
        room.pause()

        state = "Playing"
        Label6.configure(text = state)

    else:
        room.play()
        state = "Paused"
        Label6.configure(text = state)
def volup():
    room.volume = room.volume + 2
    volume = room.volume + 2
    Label2.configure(text = str(volume)+"%")
    volupdate()
def voldown():
    volume = room.volume - 2
    Label2.configure(text = str(volume)+"%")
    room.volume = room.volume - 2
    volupdate()
def nex():
    try:
        room.next()
        if room.is_playing_radio == True:
            uri = room.get_current_track_info().get('uri')
            uri = uri.rsplit('/', 1)[-1]
            if uri == "CapitalMP3":
                title = "Capital FM"
            elif uri == "ClassicFMMP3":
                title = "Classic FM"
        else:           
            title = room.get_current_track_info().get('title')
            if title[:7] == "x-sonos":
                title = "Error"
        title = title.partition("-")[0]
        title = title.partition("(")[0]
        title = title.partition("[")[0]
        title = title.partition(":")[0]
        Label1.configure(text = title)
        pic = room.get_current_track_info().get(u"album_art")
        image_update(pic)
    except soco.exceptions.SoCoUPnPException:
        print("Error skipping track")
        Label1.configure(fg="red",text = "Error skipping track")

def prev():
    try:
        room.previous()
        if room.is_playing_radio == True:
            uri = room.get_current_track_info().get('uri')
            uri = uri.rsplit('/', 1)[-1]
            if uri == "CapitalMP3":
                title = "Capital FM"
            elif uri == "ClassicFMMP3":
                title = "Classic FM"
        else:           
            title = room.get_current_track_info().get('title')
            if title[:7] == "x-sonos":
                title = "Error"
        title = title.partition("-")[0]
        title = title.partition("(")[0]
        title = title.partition("[")[0]
        title = title.partition(":")[0]
        Label1.configure(text = title)
        pic = room.get_current_track_info().get(u"album_art")
        image_update(pic)
    except soco.exceptions.SoCoUPnPException:
        print("Error skipping track")
        Label1.configure(fg="red", text = "Error skipping track")

def mute():
    room.mute = True
    Label2.configure(fg="red",text="MUTED")
    my_picture = "0.png"
    image = PIL.Image.open(my_picture)
    pil_img = image.resize((50, 50))
    tk_img = ImageTk.PhotoImage(pil_img)
    #
    panel2.configure(image=tk_img)
    panel2.image = tk_img
def unmute():
    room.mute = False
    volume = room.volume
    Label2.configure(fg="white",text = str(volume)+"%")
    
def volupdate():
    #Coloured volume image
    volume = room.volume

    if volume <= 5:
        my_picture = "1.png"
        image = PIL.Image.open(my_picture)
        pil_img = image.resize((50, 50))
        tk_img = ImageTk.PhotoImage(pil_img)
        #
        panel2.configure(image=tk_img)
        panel2.image = tk_img
    elif volume > 5 and volume <= 10:
        my_picture = "2.png"
        image = PIL.Image.open(my_picture)
        pil_img = image.resize((50, 50))
        tk_img = ImageTk.PhotoImage(pil_img)
        #
        panel2.configure(image=tk_img)
        panel2.image = tk_img
    elif volume > 10 and volume <= 15:
        my_picture = "3.png"
        image = PIL.Image.open(my_picture)
        pil_img = image.resize((50, 50))
        tk_img = ImageTk.PhotoImage(pil_img)
        #
        panel2.configure(image=tk_img)
        panel2.image = tk_img
    elif volume > 15 and volume <= 20:
        my_picture = "4.png"
        image = PIL.Image.open(my_picture)
        pil_img = image.resize((50, 50))
        tk_img = ImageTk.PhotoImage(pil_img)
        #
        panel2.configure(image=tk_img)
        panel2.image = tk_img
    elif volume > 20 and volume <= 25:
        my_picture = "5.png"
        image = PIL.Image.open(my_picture)
        pil_img = image.resize((50, 50))
        tk_img = ImageTk.PhotoImage(pil_img)
        #
        panel2.configure(image=tk_img)
        panel2.image = tk_img
    elif volume > 25 and volume <= 30:
        my_picture = "6.png"
        image = PIL.Image.open(my_picture)
        pil_img = image.resize((50, 50))
        tk_img = ImageTk.PhotoImage(pil_img)
        #
        panel2.configure(image=tk_img)
        panel2.image = tk_img
    elif volume > 30 and volume <= 35:
        my_picture = "7.png"
        image = PIL.Image.open(my_picture)
        pil_img = image.resize((50, 50))
        tk_img = ImageTk.PhotoImage(pil_img)
        #
        panel2.configure(image=tk_img)
        panel2.image = tk_img
    elif volume > 35 and volume <= 40:
        my_picture = "8.png"
        image = PIL.Image.open(my_picture)
        pil_img = image.resize((50, 50))
        tk_img = ImageTk.PhotoImage(pil_img)
        #
        panel2.configure(image=tk_img)
        panel2.image = tk_img
def image_update(pic):
    my_page = urlopen(pic)
    my_picture = io.BytesIO(my_page.read())
    image = PIL.Image.open(my_picture)
    pil_img = image.resize((180, 180))
    tk_img = ImageTk.PhotoImage(pil_img)
    panel.configure(image=tk_img)
    panel.image = tk_img
def callback():
    if room.is_playing_radio == True:
        uri = room.get_current_track_info().get('uri')
        uri = uri.rsplit('/', 1)[-1]
        if uri == "CapitalMP3":
            pic = "https://images-eu.ssl-images-amazon.com/images/I/41M6314yn5L.png"
            title = "Capital FM"
        elif uri == "ClassicFMMP3":
            pic = "https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/e8/cd/89/e8cd898b-d283-1140-f3f1-6fe6894ffc4f/AppIcon-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-6.png/246x0w.jpg"
            title = "Classic FM"
    else:
        
        pic = room.get_current_track_info().get(u"album_art")
        if pic == "":
            pic = "https://lh6.googleusercontent.com/-Px2Steg_XRM/AAAAAAAAAAI/AAAAAAAAFa4/kpB3EVdNHGw/s0-c-k-no-ns/photo.jpg"
            
        title = room.get_current_track_info().get('title')
        if title[:7] == "x-sonos":
            title = "Error"
    image_update(pic)

    
    title = title.partition("-")[0]
    title = title.partition("(")[0]
    title = title.partition("[")[0]
    title = title.partition(",")[0]
    title = title.partition(":")[0]
    Label1.configure(fg="white",text = title)
    length = len(title)
    artist = room.get_current_track_info().get('artist')
    artist = artist.partition(":")[0]
    artist = "Artist: " + artist
    
    Label3.configure(text = artist)   

    zone = room.get_speaker_info().get('zone_name')
    root.title("Sonos Controller | In " + zone + " | Playing: " + title)

    pos = room.get_current_track_info().get('position')
    pos = "| " + str(pos) + " |"

    volupdate()

    album = room.get_current_track_info().get('album')
    album = album.partition("-")[0]
    album = album.partition("(")[0]
    album = album.partition("[")[0]
    album = title.partition(",")[0]
    album = title.partition(":")[0]
    album = "Album: " + album
    Label5.configure(text = album)

    state = room.get_current_transport_info().get('current_transport_state')
    if state == "PLAYING":
        state = "Playing"
    else:
        state = "Paused"
    Label6.configure(text = state)
    volupdate()
    root.after(3000, callback)


def fan():
    global items
    global fan_item
    fan_state = items.get('smart_plug_2')

    if fan_state.state == "ON":
        fan_item.off()
    else:
        fan_item.on()
    
def globe():
    global items
    global globe_item
    globe_state = items.get('fan')
    if globe_state.state == "ON":
        globe_item.off()
    else:
        globe_item.on()

def hue_main():
    state = str(b.get_light(1,'on'))
    if state == "False":
        b.set_light(1,'on', True)
    elif state == "True":
        b.set_light(1,'on',False)


def hue_monitors():
    state = str(b.get_light(2,'on'))
    if state == "False":
        b.set_light(2,'on', True)
    elif state == "True":
        b.set_light(2,'on',False)
        
        


zone = room.get_speaker_info().get('zone_name')


root = Tk()
root.geometry("500x325")
#root.resizable(0, 0)
root.title("Sonos Controller | In " + zone)
root.configure(background='black')


root.iconbitmap('photo.ico')


title = room.get_current_track_info().get('title')
duration = room.get_current_track_info().get('duration')

if title[:7] == "x-sonos":
    title == "Error"

else:
    title = title.partition("-")[0]
    title = title.partition("(")[0]
    title = title.partition("[")[0]
    title = title.partition(",")[0]
    title = title.partition(":")[0]
artist = "Artist: " + room.get_current_track_info().get('artist')
volume = str(room.volume)

#
#Album Art
if room.is_playing_radio == True:
    uri = room.get_current_track_info().get('uri')
    uri = uri.rsplit('/', 1)[-1]
    if uri == "CapitalMP3":
        pic = "https://images-eu.ssl-images-amazon.com/images/I/41M6314yn5L.png"
        title = "Capital FM"
    elif uri == "ClassicFMMP3":
        pic = "https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/e8/cd/89/e8cd898b-d283-1140-f3f1-6fe6894ffc4f/AppIcon-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-6.png/246x0w.jpg"
        title = "Classic FM"      
else:  
    pic = room.get_current_track_info().get(u"album_art")
    if pic == "":
        pic = "https://lh6.googleusercontent.com/-Px2Steg_XRM/AAAAAAAAAAI/AAAAAAAAFa4/kpB3EVdNHGw/s0-c-k-no-ns/photo.jpg"

       
my_page = urlopen(pic)
my_picture = io.BytesIO(my_page.read())
image = PIL.Image.open(my_picture)
pil_img = image.resize((180, 180))
tk_img = ImageTk.PhotoImage(pil_img)
#
panel = Label(root, bg="white", image=tk_img)
panel.grid(row=3, column=0, sticky=W)
panel.configure(image=tk_img)
panel.image = tk_img

volume = room.volume
volume = str(volume) + "%"

#Volume Image
my_picture = "1.png"
image = PIL.Image.open(my_picture)
pil_img = image.resize((50, 50))
tk_img = ImageTk.PhotoImage(pil_img)
#
panel2 = Label(root, bg="white", image=tk_img)
panel2.grid(row=0, column=3, sticky=W)
panel2.configure(image=tk_img)
panel2.image = tk_img


#Labels and Buttons

#Title
Label1 = Label(root, fg="white", bg="black", font=("Noto Serif", 16), text = title)
Label1.grid(row=0, column=0, sticky=W)
f = font.Font(Label1, Label1.cget("font"))
f.configure(underline = True)
Label1.configure(font=f)

#Volume
Label2 = Label(root, fg="white",bg="black", font=("Noto Serif", 12), text = volume)
Label2.grid(row=0, column=2, sticky=W)

#Artist
Label3 = Label(root, fg="white",bg="black", font=("Noto Serif", 11), text = artist)
Label3.grid(row=1, column=0, sticky=W)
album = room.get_current_track_info().get('album')
album = album.partition("-")[0]
album = album.partition("(")[0]
album = album.partition("[")[0]
album = title.partition(",")[0]
album = title.partition(":")[0]

album = "Album: " + album
Label5 = Label(root, fg="white",bg="black", font=("Noto Serif" , 11), text = album)
Label5.grid(row=2, column=0, sticky=W)

pos = room.get_current_track_info().get('position')
pos = "| " + str(pos) + " |"


state = room.get_current_transport_info().get('current_transport_state')

if state == "PLAYING":
    state = "Playing"
else:
    state = "Paused"
    
Label6 = Label(root, fg="white",bg="black", font=("Noto Serif", 10), text = state)
Label6.grid(row=3, column=1, sticky=W)



#Button Images
playimg=PhotoImage(file="play.png")
volupimg=PhotoImage(file="volup.png")
voldownimg=PhotoImage(file="voldown.png")
nextimg=PhotoImage(file="next.png")
previmg=PhotoImage(file="prev.png")

#Buttons
Button1 = Button(root, bg = "black",border = "0", image=playimg,command=play, height = 80, width = 80).grid(row=3, column=2, sticky=W)
Button(root, bg = "black", border = "0", image = volupimg,command=volup).grid(row=0, column=1, sticky=W)
Button(root, bg = "black", border = "0", image = voldownimg,command=voldown).grid(row=1, column=1, sticky=W)
Button(root, bg = "black", border = "0", image = nextimg,command=nex).grid(row=2, column=2, sticky=W)
Button(root, bg = "black", border = "0", image = previmg,command=prev).grid(row=2, column=1, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="Unmute",command=unmute).grid(row=2, column=3, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="  Mute  ",command=mute).grid(row=1, column=3, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="Olly's Bedroom",command=bedroom).grid(row=2, column=4, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="Kitchen",command=kitchen).grid(row=1, column=4, sticky=W)

Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="Fan",command=fan).grid(row=3, column=3, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="Globe",command=globe).grid(row=3, column=4, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="Light",command=hue_main).grid(row=3, column=5, sticky=W)
Button(root, fg="white",bg="black", borderwidth = "1", font=("Noto Serif", 10), text="Monitors",command=hue_monitors).grid(row=3, column=6, sticky=W)

root.after(1, callback)
root.mainloop()





