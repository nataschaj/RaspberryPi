
import smbus
import time
import RPi.GPIO as GPIO
import threading
from threading import Thread

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

global ligthMeasure
lightMeasure = 0

def StartLight():
 print("startlight function started")
 bus = smbus.SMBus(1)
 bus.write_byte(0x48, 0x00)

 while(True):
  print("started measuring")
  lightMeasure = bus.read_byte(0x48)

  if (lightMeasure < 210):
   # tænder lampen
   GPIO.output(18, GPIO.HIGH)
   print("18 high")
  if (lightMeasure >210):
   GPIO.output(18, GPIO.LOW)
   print("18 low")
   waveArm()
   print("waveArm")
   #Thread(target=waveArm).start()
   #print(lightMeasure)
 time.sleep(2)

def waveArm():
 pwm = GPIO.PWM(17, 50)
 pwm.start(7)
 for i in range(0,180):
  DC=1./10.*(i)+2
  pwm.ChangeDutyCycle(DC)
  time.sleep(0.001)
 for i in range(180,0, -1):
  DC=1./100.*i +2
  pwm.ChangeDutyCycle(DC)

StartLight()
#waveArm()
#try:
#       Thread(target=StartLight).start()
#       Thread(target=StartWave).start()

#except:
#       print("Threading did not work")
