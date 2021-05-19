# Import libraries
import RPi.GPIO as GPIO
import time


# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)


# Set pin as an output, and define as servo as PWM pin
# Servo 1
GPIO.setup(37,GPIO.OUT)
servo1 = GPIO.PWM(37,50)

# Servo 2
GPIO.setup(35,GPIO.OUT)
servo2 = GPIO.PWM(35,50)

# Servo 3
GPIO.setup(33,GPIO.OUT)
servo3 = GPIO.PWM(33,50)

# Servo 4
GPIO.setup(31,GPIO.OUT)
servo4 = GPIO.PWM(31,50)


# Start PWM running, with value of 0 (pulse off)
servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)


try:
    while True:
        num_servo = int(input('Pls write num of servo which u want move: '))

        if num_servo == 1:
            #Ask user for angle and turn servo to it
            angle = float(input('Enter for servo1 angle between 0 & 180: '))
            servo1.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)


        elif num_servo == 2:
            #Ask user for angle and turn servo to it
            angle = float(input('Enter for servo2 angle between 0 & 180: '))
            servo2.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            servo2.ChangeDutyCycle(0)


        elif num_servo == 3:
            #Ask user for angle and turn servo to it
            angle = float(input('Enter for servo3 angle between 0 & 180: '))
            servo3.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            servo3.ChangeDutyCycle(0)

        elif num_servo == 4:
            #Ask user for angle and turn servo to it
            angle = float(input('Enter for servo4 angle between 0 & 180: '))
            servo4.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            servo3.ChangeDutyCycle(0)

        else:
            print("I don't understand u")

INIT = 0
IDLE = 1
EXEC = 2

state = INIT

if state is INIT:
    # initialize
    state = IDLE

if state is IDLE:
    # write to servo by num
    state = EXEC

if state is EXEC:
    # initialize
    state = INIT



finally:
    #Clean things up at the end
    servo1.stop()
    servo2.stop()
    servo3.stop()
    servo4.stop()
    GPIO.cleanup()
    print("Servo Stop")
