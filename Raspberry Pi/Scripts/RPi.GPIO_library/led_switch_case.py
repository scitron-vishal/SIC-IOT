import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
 
pin1 =2
pin2= 3
sw = 4
 
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)
gpio.setup(sw, gpio.IN)
#gpio.output(pin1, gpio.HIGH)
#gpio.output(pin2, gpio.HIGH)
while True:
    if( gpio.input(sw) == 1):
        gpio.output(pin1, gpio.LOW)
        gpio.output(pin2, gpio.HIGH)
        
    
    else:
        gpio.output(pin1, gpio.HIGH)
        gpio.output(pin2, gpio.LOW)
    