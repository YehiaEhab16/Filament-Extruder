import RotaryEncoder as Encoder
import time
import LCD
import Thermocouple
import DC_Motor as Motor
import Heater

op_flag=1      #operation flag (0->operation mode, 1->modify mode)
st_flag=0      #Flag to determine whether to edit in Temp or RPM
act_temp=0     #Actual temperature read from Thermocouple
temp=100       #Output Temperature to Heaters
rpm=100        #Output RPM to Motor
delay_time=3   #delay time at welcome
lastInterruptTime = 0  #Measuring Interrupt time to interrupts overlapping by encoder 

#ISR for SW (switches from modify or operation mode)
def SW_ISR():
    global op_flag,st_flag
    if op_flag == 0:
        #stopping motor and heater during modification
        Motor.Rotate(0)
        Heater.Heat(0)
        print("Switched to modify mode")
        op_flag = 1

    else:
        if (st_flag == 1):
            print("Switched to operation mode")
            op_flag = 0
            st_flag = 0
        else:
            st_flag += 1
 
#ISR for CLK (to edit in temp and rpm values) 
def CLK_ISR():
    global op_flag,st_flag,temp,rpm,lastInterruptTime
    
    #Measuring interrupt time 
    interruptTime = time.ticks_ms()

    #Detemining whether the encoder is turning right or left
    if (time.ticks_diff(interruptTime, lastInterruptTime) > 20):
        if (Encoder.DT_read() == 0):
            print("Right Turn")
            if(st_flag==0 and op_flag==1):
                temp+=1
            elif(st_flag==1):
                rpm+=1
        else:
            print("Left Turn");
            if(st_flag==0 and op_flag==1):
                temp-=1
            elif(st_flag==1):
                rpm-=1
    #Updating last interrupt time
    lastInterruptTime = interruptTime

#Intializing encoder after deifining its ISRs
Encoder.Init(SW_ISR,CLK_ISR)

#Welcoming user
LCD.Welcome(delay_time)

while True: 
    #Displaying temp and rpm
    LCD.DispVars(act_temp,temp,rpm)
    
    #Output during operation mode
    if(op_flag==0):
        Motor.Rotate(rpm)
        Heater.Heat(temp)
    
    #Reading temp from thermocouple
    act_temp = Thermocouple.Read();

    #Specifying the place where the user can edit
    if(op_flag==1):
        if(st_flag==0):
            LCD.DispPos("<--",12,0)
        else:
            LCD.DispPos("   ",12,0)
            LCD.DispPos("<--",12,1)
    else:
        LCD.DispPos("   ",12,1)
