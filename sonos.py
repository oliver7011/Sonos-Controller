import soco
from soco import SoCo
import time

from soco.discovery import by_name
device = by_name("Kitchen")
print(device)
