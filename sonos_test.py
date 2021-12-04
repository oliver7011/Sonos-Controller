import soco
from soco import SoCo
import time

room = SoCo("192.168.1.41")

while True:
    pic = room.get_current_track_info().get(u"album_art")
    print(pic)
    time.sleep(2)
