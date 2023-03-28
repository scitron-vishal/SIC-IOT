from  gpiozero import Motionsensor
import time
pir =Motionsensor(4)
print("waiting for PIR to settle")
pir.wait_for_no_motion()
while True :
    print("Ready")
    pir.wait_for_motion()
    print("Motion detected!")
    time.sleep(1)