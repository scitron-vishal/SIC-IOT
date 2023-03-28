import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
pin1 = 2
pin2 = 3
pin3 = 4
while True:
    gpio.setup(pin1, gpio.OUT)
    gpio.output(pin1, gpio.HIGH)
    sleep(1)
    gpio.output(pin1, gpio.LOW)
    sleep(1)
    
    
    