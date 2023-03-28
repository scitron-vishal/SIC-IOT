from gpiozero import Button, LED
from time import sleep

l1 = LED(2)
l2 = LED(3)
l3 = LED(4)
l4 = LED(5)
l5 = LED(6)
btn = Button(14)



while True:
   l5.off()
   l1.on()
   sleep(0.3)
   l1.off()
   l2.on()
   sleep(0.3)
   l2.off()
   l3.on()
   sleep(0.3)
   l3.off()
   l4.on()
   sleep(0.3)
   l4.off()
   l5.on()
   sleep(0.3)