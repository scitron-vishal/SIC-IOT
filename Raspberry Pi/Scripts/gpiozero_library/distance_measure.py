from gpiozero import LED, DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=17,trigger=3)
led =LED(2)
while True :
    distance=sensor.distance*100
    print("distance",distance)
    if distance<10:
        led.on()
        
else:
            led.off()
            sleep(1)