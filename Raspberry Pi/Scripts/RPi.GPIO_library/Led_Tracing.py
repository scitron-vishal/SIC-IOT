import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

l1 =2
l2=3
l3=4
l4=5
l5=6

gp.setup(l1,gp.OUT)
gp.setup(l2,gp.OUT)
gp.setup(l3,gp.OUT)
gp.setup(l4,gp.OUT)
gp.setup(l5,gp.OUT)

while True:
    gp.output(l1,gp.HIGH)
    sleep(0.1)
    gp.output(l1,gp.LOW)
    
    gp.output(l2,gp.HIGH)
    sleep(0.1)
    gp.output(l2,gp.LOW)
    
    gp.output(l3,gp.HIGH)
    sleep(0.1)
    gp.output(l3,gp.LOW)
    
    
    gp.output(l4,gp.HIGH)
    sleep(0.1)
    gp.output(l4,gp.LOW)
    
    
    gp.output(l5,gp.HIGH)
    sleep(0.1)
    gp.output(l5,gp.LOW)
    
