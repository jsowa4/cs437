from sense_hat import SenseHat
from time import sleep
import sys

sense=SenseHat()

blue= (0,0,255)
yellow= (255,255,0)
red=(255,0,0)

x, y = 3, 5



while True:
    for event in sense.stick.get_events():
        sense.clear()
        sense.set_pixel(x, y, red)
        if event.action == 'pressed' and event.direction == 'middle':
            sense.clear()
            sys.exit(0)
        if event.action == 'pressed' and event.direction == 'up':
            if y > 0:
                y -= 1
        if event.action == 'pressed' and event.direction == 'down':
            if y < 7:
                y += 1
        if event.action == 'pressed' and event.direction == 'right':
            if x < 7:
                x += 1
        if event.action == 'pressed' and event.direction == 'left':
            if x > 0:
                x-= 1
   
   
  
  
   