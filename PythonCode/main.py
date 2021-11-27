import RotaryEncoder as Encoder
import time
import LCD

op_flag=0 #operation
st_flag=0
temp=100
rpm=100
lastInterruptTime = 0

def SW_ISR():
    global op_flag,st_flag
    if op_flag == 0:
#     Heater(0)
#     Motor_Rotate(0)
        print("Switched to modify mode")
        op_flag = 1

    else:
        if (st_flag == 1):
            print("Switched to operation mode")
            op_flag = 0
            st_flag = 0
        else:
            st_flag += 1
    
def CLK_ISR():
    global op_flag,st_flag,temp,rpm,lastInterruptTime
    
    interruptTime = time.ticks_ms()
    
    print(time.ticks_diff(interruptTime, lastInterruptTime))

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
    lastInterruptTime = interruptTime

Encoder.Init(SW_ISR,CLK_ISR)

LCD.DispPos("Welcome to",3,0)
LCD.DispPos("Extruder",4,1)
time.sleep(1)
LCD.Clear()
Lcd.Disp("Temp:")
LCD.DispPos("RPM:",0,1)

while True:
    pass
