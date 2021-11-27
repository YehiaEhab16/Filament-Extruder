#importing system modules
from machine import Pin

#Required Pins
SW_pin = 14
DT_pin = 12
CLK_pin = 13

#Initializing Pins as input pullup
SW = Pin(SW_pin, Pin.IN, Pin.PULL_UP)
DT = Pin(DT_pin, Pin.IN, Pin.PULL_UP)
CLK = Pin(CLK_pin, Pin.IN, Pin.PULL_UP)

#Global Functions for callback
def Global_Function1():
    pass

def Global_Function2():
    pass

#Function to read DT pin (to determine direction of rotation)
def DT_read():
    return DT.value()

#Function to initialize Encoder and take the ISRs from user
def Init(SW_Callback, CLK_back):
    global Global_Function1,Global_Function2
    
    Global_Function1 = SW_Callback
    Global_Function2 = CLK_back
    
    SW.irq(trigger=Pin.IRQ_RISING, handler=SW_ISR)
    CLK.irq(trigger=Pin.IRQ_FALLING, handler=CLK_ISR)
    

#ISR for SW pin (the interrupt is disabled within ISR to avoid debouncing)
def SW_ISR(pin):
    SW.irq(trigger=0, handler=SW_ISR)
    global Global_Function1
    Global_Function1()
    SW.irq(trigger=Pin.IRQ_RISING, handler=SW_ISR)
   
#ISR for CLK pin (the interrupt is disabled within ISR to avoid debouncing)   
def CLK_ISR(pin):
    CLK.irq(trigger=0, handler=CLK_ISR)
    global Global_Function2
    Global_Function2()
    CLK.irq(trigger=Pin.IRQ_FALLING, handler=CLK_ISR)