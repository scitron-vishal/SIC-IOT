import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
red=2
yellow=3
green=4
sw=5

gpio.setup(red,gpio.OUT)
gpio.setup(yellow,gpio.OUT)
gpio.setup(green,gpio.OUT)
gpio.setup(sw,gpio.IN)

while True:
    if(gpio.input(sw)==1):
        gpio.output(red,gpio.LOW)
        gpio.output(green,gpio.LOW)
        gpio.output(yellow,gpio.HIGH)
        sleep(1)
        gpio.output(red,gpio.HIGH)
        gpio.output(green,gpio.LOW)
        gpio.output(yellow,gpio.LOW)
        sleep(3)
        gpio.output(red,gpio.LOW)
        gpio.output(green,gpio.LOW)
        gpio.output(yellow,gpio.HIGH)
        sleep(1)
    
    else:
        gpio.output(red,gpio.LOW)
        gpio.output(green,gpio.HIGH)
        gpio.output(yellow,gpio.LOW)

