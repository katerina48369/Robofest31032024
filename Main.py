from time import sleep
import keyboard
motor10=14
motor11=15
motor20=24
motor21=23
motor30=27
motor31=17
motor40=25
motor41=22

updates =30
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(motor10,GPIO.OUT)
GPIO.setup(motor11,GPIO.OUT)
GPIO.setup(motor20,GPIO.OUT)
GPIO.setup(motor21,GPIO.OUT)
GPIO.setup(motor30,GPIO.OUT)
GPIO.setup(motor31,GPIO.OUT)
GPIO.setup(motor40,GPIO.OUT)
GPIO.setup(motor41,GPIO.OUT)

    
GPIO.output(motor10,GPIO.LOW)
GPIO.output(motor20,GPIO.LOW)
GPIO.output(motor11,GPIO.LOW)
GPIO.output(motor21,GPIO.LOW)

GPIO.output(motor31,GPIO.LOW)
GPIO.output(motor41,GPIO.LOW)
GPIO.output(motor30,GPIO.LOW)
GPIO.output(motor40,GPIO.LOW)

s1=8
s2=7
s3=5
GPIO.setup(s1, GPIO.OUT)
servo1=GPIO.PWM(s1,50)
GPIO.setup(s1, GPIO.OUT)
servo2=GPIO.PWM(s2,50)
GPIO.setup(s1, GPIO.OUT)
servo3=GPIO.PWM(s3,50)
servo2.start(0)
servo1.start(0)
servo3.start(0)

while True:
           
        
  

    if keyboard.is_pressed('w'):
    
        GPIO.output(motor10,GPIO.HIGH)
        GPIO.output(motor11,GPIO.HIGH)
        GPIO.output(motor20,GPIO.HIGH)
        GPIO.output(motor30,GPIO.HIGH)
        GPIO.output(motor40,GPIO.HIGH)

  


    elif keyboard.is_pressed('s'):

        GPIO.output(motor10,GPIO.HIGH)
        GPIO.output(motor21,GPIO.HIGH)
        GPIO.output(motor20,GPIO.HIGH)
        GPIO.output(motor30,GPIO.HIGH)
        GPIO.output(motor31,GPIO.HIGH)
        GPIO.output(motor40,GPIO.HIGH)
        GPIO.output(motor21,GPIO.HIGH)


    elif keyboard.is_pressed('d'):
        GPIO.output(motor10,GPIO.HIGH)
        GPIO.output(motor21,GPIO.HIGH)
        GPIO.output(motor20,GPIO.HIGH)
        GPIO.output(motor40,GPIO.HIGH)
        GPIO.output(motor30,GPIO.HIGH)

  
        
    elif keyboard.is_pressed('a'):

        GPIO.output(motor10,GPIO.HIGH)
        GPIO.output(motor11,GPIO.HIGH)
        GPIO.output(motor20,GPIO.HIGH)
        GPIO.output(motor40,GPIO.HIGH)
        GPIO.output(motor30,GPIO.HIGH)
        GPIO.output(motor41,GPIO.HIGH)
        GPIO.output(motor31,GPIO.HIGH)
    elif keyboard.is_pressed('q'):
        servo1.ChangeDutyCycle(11)
    elif keyboard.is_pressed('r'):
        servo1.ChangeDutyCycle(2)
    elif keyboard.is_pressed('1'):
        servo2.ChangeDutyCycle(11)
        servo3.ChangeDutyCycle(2)
    elif keyboard.is_pressed('2'):
        servo2.ChangeDutyCycle(2)
        servo3.ChangeDutyCycle(11)
    else:
        GPIO.output(motor10,GPIO.LOW)
        GPIO.output(motor20,GPIO.LOW)
        GPIO.output(motor11,GPIO.LOW)
        GPIO.output(motor21,GPIO.LOW)

        GPIO.output(motor31,GPIO.LOW)
        GPIO.output(motor41,GPIO.LOW)
        GPIO.output(motor30,GPIO.LOW)
        GPIO.output(motor40,GPIO.LOW)

 
    sleep(1/updates)
    pass
