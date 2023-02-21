import RPi.GPIO as GPIO
import time
import ADC0834
from  time import sleep
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 5
GPIO_ECHO = 6
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
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

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1 = {'EN': 25, 'input1': 24, 'input2': 23}
Motor2 = {'EN': 17, 'input1': 27, 'input2': 22}

for x in Motor1:
    GPIO.setup(Motor1[x], GPIO.OUT)
    GPIO.setup(Motor2[x], GPIO.OUT)

EN1 = GPIO.PWM(Motor1['EN'], 100)    
EN2 = GPIO.PWM(Motor2['EN'], 100)    

EN1.start(0)
EN2.start(0)

while True:
    for x in range(40, 100):
        print ("FORWARD MOTION")
        EN1.ChangeDutyCycle(x)
        EN2.ChangeDutyCycle(x)

        GPIO.output(Motor1['input1'], GPIO.HIGH)
        GPIO.output(Motor1['input2'], GPIO.LOW)
        
        GPIO.output(Motor2['input1'], GPIO.HIGH)
        GPIO.output(Motor2['input2'], GPIO.LOW)
	dist = distance()
        cprint ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)
        sleep(0.1)
   
    print ("STOP")
    EN1.ChangeDutyCycle(0)
    EN2.ChangeDutyCycle(0)

    sleep(5)
     
    for x in range(40, 100):
        print ("BACKWARD MOTION")
        EN1.ChangeDutyCycle(x)
        EN2.ChangeDutyCycle(x)
        
        GPIO.output(Motor1['input1'], GPIO.LOW)
        GPIO.output(Motor1['input2'], GPIO.HIGH)

        GPIO.output(Motor2['input1'], GPIO.LOW)
        GPIO.output(Motor2['input2'], GPIO.HIGH)

        sleep(0.1)
     
    print ("STOP")
    EN1.ChangeDutyCycle(0)
    EN2.ChangeDutyCycle(0)

    sleep(5)

GPIO.cleanup()
