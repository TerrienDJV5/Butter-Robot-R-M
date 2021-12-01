# Write your code here :-)
from gpiozero import LED
from time import sleep


import RPi.GPIO as GPIO
import time

led = LED(18)


servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

servoRotation = [5,7.5,10,12.5,10,7.5,5,2.5]
servoTiming = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
setServoI = 0

while True:
    led.on()
    #time.sleep(1)
    led.off()
    #time.sleep(1)
    print(time.time())

    try:
        p.ChangeDutyCycle(servoRotation[setServoI])
        time.sleep(servoTiming[setServoI])
        #p.ChangeDutyCycle(5)
        #time.sleep(0.5)
        #p.ChangeDutyCycle(7.5)
        #time.sleep(0.5)
        #p.ChangeDutyCycle(10)
        #time.sleep(0.5)
        #p.ChangeDutyCycle(12.5)
        #time.sleep(0.5)
        #p.ChangeDutyCycle(10)
        #time.sleep(0.5)
        #p.ChangeDutyCycle(7.5)
        #time.sleep(0.5)
        #p.ChangeDutyCycle(5)
        #time.sleep(0.5)
        #p.ChangeDutyCycle(2.5)
        #time.sleep(0.5)
        setServoI += 1
        if setServoI>= len(servoRotation):
            setServoI = 0
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()


