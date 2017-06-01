import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  
GPIO.setup(3, GPIO.OUT)

while true:
      k=GPIO.input(27)
      if k==0:
            print ("there are no intruders")
            GPIO.output(27, 0)
            sleep(1)
           
      elif k==1:
            print ("there is an intruder")
            GPIO.output(27, 1)
            sleep.(1)
            
            
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)


GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(16, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT)

while true:
      
      key=input("Enter a control. You can choose from W, A, S or D ")
      
      if key=="w":
            GPIO.output(27, GPIO.HIGH)
            sleep(1)
            GPIO.output(27, GPIO.LOW)
            
            timer=0
            
            while timer <5:
            
               sensor=GPIO.input(25)
            
               if sensor==1:
                  print("There is nothing there")
                  sleep(0.1)
            
               elif sensor==0:
                  print("There is something there")
                  GPIO.output(27, GPIO.LOW)
                  GPIO.output(25, GPIO.LOW)
               elif timer =5:
                  break
            
               timer = timer + 1
               
