import RPi.GPIO as gp
from time import sleep
import time

gp.setmode(gp.BCM)
gp.setup(17,gp.OUT)
gp.setup(18,gp.IN)

try:
    stop=0
    while True:
        gp.output(17,False)
        sleep(0.5)
        
        gp.output(17,True)
        sleep(0.00001)
        gp.output(17,False)
        
        while gp.input(18)==0:
            start=time.time()
            
        while gp.input(18)==1:
            stop=time.time()
            
        time_interval=stop - start
        distance=time_interval*17000
        distance=round(distance,2)
        
        print(f"distance :{distance}")
        
except keyboardInterrupt:
    gp.cleanup()