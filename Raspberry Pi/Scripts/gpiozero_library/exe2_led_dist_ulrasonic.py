from gpiozero import LED, DistanceSensor
from time import sleep

sensor = DistanceSensor(echo = 21,trigger =20 )
red= LED(2)
gre= LED(3)
amb= LED(4)

                
while True :
	distance = sensor.distance * 100 
	print("distance : " , distance)
	if(distance <10):
		red.on()
		amb.off()
		gre.off()
	elif (distance > 10 and distance < 20): 
		red.off()
		amb.on()
		gre.off()
	else :
                   gre.on()
                   amb.off()
                   red.off()
	sleep(0.2)
        
        
	
		

