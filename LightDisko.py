
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

count = 0
while(count < 100) :
        count = count +1
        GPIO.output(14, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(14, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(14, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(18,GPIO.LOW)
GPIO.cleanup()






