from gpiozero import LED,Button
from time import sleep
import random

led=LED(2)
sw1=Button(3)
sw2=Button(4)

while True:
#    time=random.uniform(1,3)
 #  sleep(time)
   sleep(2)
   led.on()
    
    while True:
        if  sw1.is_pressed:
            print("player_1 wins")
            break
        if  sw2.is_pressed:
            print("player_2 wins")
            break
    led.off()
        