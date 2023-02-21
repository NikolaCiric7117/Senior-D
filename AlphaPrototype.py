import RPi.GPIO as GPIO
import ADC0834
from time import sleep
import time
#Motor Setup 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor2 = {'EN': 17, 'input1': 27, 'input2': 22}

for x in Motor2:
    
    GPIO.setup(Motor2[x], GPIO.OUT)

  
EN2 = GPIO.PWM(Motor2['EN'], 100)    

                 
EN2.start(0)                    
#Ultrasonic Sensor Setup
GPIO_TRIGGER = 5
GPIO_ECHO = 6
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#Distance Function
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
#Joystick Setup
BtnPin = 22
def setup():
	# Set the GPIO modes to BCM Numbering
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	ADC0834.setup()

def destroy():
	# Release resource
	GPIO.cleanup()

setup()
while True:
    dist = distance()
    x_val = ADC0834.getResult(0)
    y_val = ADC0834.getResult(1)
    if(dist > 20):

        
         if(y_val >131):
            GPIO.setup(22,GPIO.OUT)
            print("forwards")
            print((y_val/255)*100)
            motor_speed = (y_val/255) *100
            EN2.ChangeDutyCycle(motor_speed)
            GPIO.output(Motor2['input1'], GPIO.HIGH)
            GPIO.output(Motor2['input2'], GPIO.LOW)
      
    else:
        if(y_val <123):
            print("backwards")
            print((y_val/255)*100)
            GPIO.setup(22,GPIO.OUT)
            GPIO.output(Motor2['input1'], GPIO.LOW)
            GPIO.output(Motor2['input2'], GPIO.HIGH)
           # EN2.ChangeDutyCycle(255-y_val)
        else:
            print("stopped")
            EN2.ChangeDutyCycle(0)
GPIO.cleanup()

   