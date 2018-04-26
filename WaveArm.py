

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin = 11
GPIO.setup(servoPin,GPIO.OUT)
pwm =GPIO.PWM(servoPin,50)
pwm.start(7)
while(1):
        for i in range(0,180):
                DC=1./10.*(i)+2
                pwm.ChangeDutyCycle(DC)
                time.sleep(0.001)
        for i in range(180,0, -1):
                DC=1./100.*i +2
                pwm.ChangeDutyCycle(DC)
                time.sleep(0.001)

pwm.stop()
GPIO.cleanup()





