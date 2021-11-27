#importing system modules
from machine import Pin,PWM

#Required Pins
Motor_pin = 0

#Initializing Pins as oputput
Motor = Pin(Motor_pin, Pin.OUT)

#Configuring PWM pins
pwm = PWM(Pin(Motor_pin), freq=1000)


#Max motor RPM
Max_RPM=200.0

#Function that outputs pwm signals to the heaters
def Rotate(rpm):
    out = int((rpm/Max_RPM)*1023.0)
    pwm.duty(out)