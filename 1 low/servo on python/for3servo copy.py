# Import libraries
import RPi.GPIO as GPIO
import time


INIT = 0
IDLE = 1
EXEC = 2

state = INIT

while True:
    if state is INIT:

        servo1 = 8
        servo2 = 10
        servo3 = 12

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(servo1,GPIO.OUT)
        GPIO.setup(servo2,GPIO.OUT)
        GPIO.setup(servo3,GPIO.OUT)

        
        s1 = GPIO.PWM(servo1,50)
        s2 = GPIO.PWM(servo2,50)
        s3 = GPIO.PWM(servo3,50)


        s1.start(0)
        s2.start(0)
        s3.start(0)

        num_servo = int(input('Введите номер сервопривода от 1 до 3: '))

        state = IDLE

    if state is IDLE:
        if num_servo == 1:
            angle = float(input('Введите число от 0 до 180 для servo1: '))
            s1.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            s1.ChangeDutyCycle(0)

        elif num_servo == 2:
            angle = float(input('Введите число от 0 до 180 для servo2: '))
            s2.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            s2.ChangeDutyCycle(0)

        elif num_servo == 3:
            angle = float(input('Введите число от 0 до 180 для servo3: '))
            s3.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            s3.ChangeDutyCycle(0)

        else:
            print("Я не понимаю вас")

        state = EXEC

    if state is EXEC:
        # initialize
        state = INIT



# finally:
#     #Clean things up at the end
#     s1.stop()
#     s2.stop()
#     s3.stop()
#     GPIO.cleanup()
