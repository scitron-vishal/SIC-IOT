import RPi .GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
red=3
gpio.setup(red,gpio.OUT)

gpio.setmode(gpio.BOARD)
yellow=5
gpio.setup(yellow,gpio.OUT)

gpio.setmode(gpio.BOARD)
green=7
gpio.setup(green,gpio.OUT)

while True:
  gpio.output(red,gpio.HIGH)
  time.sleep(2)
  gpio.output(red,gpio.LOW)

  gpio.output(yellow,gpio.HIGH)
  time.sleep(1)
  gpio.output(yellow,gpio.LOW)

  gpio.output(green,gpio.HIGH)
  time.sleep(3)
  gpio.output(green,gpio.LOW)
