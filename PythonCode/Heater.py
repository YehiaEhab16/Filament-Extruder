#importing system modules
from machine import Pin,PWM

#Required Pins
Heater1_pin = 2
# Heater2_pin = 12
# Heater3_pin = 13

#Initializing Pins as oputput
Heater1 = Pin(Heater1_pin, Pin.OUT)
# Heater2 = Pin(Heater2_pin, Pin.OUT)
# Heater3 = Pin(Heater3_pin, Pin.OUT)

#Configuring PWM pins
pwm1 = PWM(Pin(Heater1_pin), freq=1000)
# pwm2 = PWM(Pin(Heater2_pin), freq=1000)
# pwm3 = PWM(Pin(Heater3_pin), freq=1000)

#Max heater temperature
Max_Temp=400.0

#Function that outputs pwm signals to the heaters
def Heat(temp):
    out = int((temp/Max_Temp)*1023.0)
    pwm1.duty(out)
#     pwm2.duty(out)
#     pwm3.duty(out)