#conditional traffic light

from gpiozero import LED, Button
from time import sleep


red = LED(2)
yel = LED(3)
gre = LED(4)
btn = Button(5)

while True:
    if btn.is_pressed :
        gre.on()
        red.off()
        yel.off()
        
    else :
        gre.off()
        yel.on()
        sleep(2)
        yel.off()
        red.on()
        sleep(3)
        red.off()
        