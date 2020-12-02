from time import sleep
import time
from picamera import PiCamera
from datetime import datetime

camera = PiCamera(resolution=(1024,768), framerate=30)

camera.iso = 100
sleep(2)

camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g


date = datetime.now()
fname = date.strftime("%Y")+date.strftime("%m")+date.strftime("%d")+date.strftime("%H")+date.strftime("%M")+"-"
print(fname)
camera.capture_sequence([fname+'image%03d.jpg' % i for i in range(3)])