from machine import I2C, Pin 
from i2c_lcd import I2cLcd 

DEFAULT_I2C_ADDR = 0x27

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000) 
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)


def Disp(string):
    lcd.putstr(string)
    
def DispPos(string,x,y):
    lcd.move_to(x, y)
    lcd.putstr(string)

def Clear():
    lcd.clear()