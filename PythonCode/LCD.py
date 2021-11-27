#importing system modules
from machine import I2C, Pin
import time
#importing i2c_lcd library
from i2c_lcd import I2cLcd 

#Default LCD Address
DEFAULT_I2C_ADDR = 0x27

#Initializing I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000) 
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

#Function to display string on LCD
def Disp(string):
    lcd.putstr(string)

#Function to display string on LCD with exact position    
def DispPos(string,x,y):
    lcd.move_to(x, y)
    lcd.putstr(string)

#Function to clear LCD	
def Clear():
    lcd.clear()

#Function to Display at the beginning of code
def Welcome(delay_time):
    DispPos("Welcome to",3,0)
    DispPos("Extruder",4,1)
    time.sleep(delay_time)
    Clear()
    Disp("Temp:")
    DispPos("RPM:",0,1)

#Function to Display required variables
def DispVars(act_temp,temp,rpm):
    DispPos(str(act_temp),5,0)
    Disp("/")
    Disp(str(temp))
    Disp(" ")
    DispPos(str(rpm),4,1)
    Disp(" ")