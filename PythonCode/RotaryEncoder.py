from machine import Pin

SW_pin = 14
DT_pin = 12
CLK_pin = 13

SW = Pin(SW_pin, Pin.IN, Pin.PULL_UP)
DT = Pin(DT_pin, Pin.IN, Pin.PULL_UP)
CLK = Pin(CLK_pin, Pin.IN, Pin.PULL_UP)

def Global_Function1():
    pass

def Global_Function2():
    pass

def DT_read():
    return DT.value()

def Init(SW_Callback, CLK_back):
    global Global_Function1,Global_Function2
    
    Global_Function1 = SW_Callback
    Global_Function2 = CLK_back
    
    SW.irq(trigger=Pin.IRQ_RISING, handler=SW_ISR)
    CLK.irq(trigger=Pin.IRQ_FALLING, handler=CLK_ISR)
    
def SW_ISR(pin):
    SW.irq(trigger=0, handler=SW_ISR)
    global Global_Function1
    Global_Function1()
    SW.irq(trigger=Pin.IRQ_RISING, handler=SW_ISR)
    
def CLK_ISR(pin):
    CLK.irq(trigger=0, handler=CLK_ISR)
    global Global_Function2
    Global_Function2()
    CLK.irq(trigger=Pin.IRQ_FALLING, handler=CLK_ISR)