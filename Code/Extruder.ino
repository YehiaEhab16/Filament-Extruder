//Including all defined libraries
#include "DC_Motor.h"
#include "LCD.h"
#include "RotaryEncoder.h"
#include "Heater.h"
#include "Thermocouple.h"

//Rotary encoder ISRs
void SW_ISR(void);
void CLK_ISR(void);

//Volatile variables to be modified inside ISRs
volatile bool op_flag = OPERATION;
volatile int st_flag = 0;

int act_temp = 0;                     //actual tempertaure to be read by thermocouple
volatile int temp = 101, rpm = 150;   //Output temperatue and RPM

void setup() {
  //Initializing all components
  LCD_Init();
  Encoder_Init(&SW_ISR,&CLK_ISR);
  Heater_Init();
  Motor_Init();
}

void loop() {
  //Displaying variables on LCD
  LCD_DisplayExactPosition(String(act_temp), 5, 0);
  LCD_Display("/");
  LCD_Display(String(temp));
  LCD_Display(" ");
  LCD_DisplayExactPosition(String(rpm), 4, 1);
  LCD_Display(" ");
  //Output only in operation mode
  if(op_flag==OPERATION)
  {
    Motor_Rotate(rpm);
    Heater(temp);
  }
  //Reading Temperature from thermocouple
  act_temp = ThermpocoupleRead();
  //Specifying place where user can edit temp and rpm
  if(op_flag==MODIFY)
  {
    if(st_flag==0)
    {
      LCD_DisplayExactPosition("<--",12,0);
    }
    else
    {
      LCD_DisplayExactPosition("   ",12,0);
      LCD_DisplayExactPosition("<--",12,1);
    }
  }
  else
    LCD_DisplayExactPosition("   ",12,1);
}

//ISR for SW pin (determine operation or modify mode)
void SW_ISR(void)
{
  Serial.println("Interrupt");
  if (op_flag == OPERATION)
  {
    //Disabling heaters and motor while modification
    Heater(0);
    Motor_Rotate(0);
    Serial.println("Switched to modify mode");
    op_flag = MODIFY;
  }
  else
  {
    if (st_flag == 1)
    {
      Serial.println("Switched to operation mode");
      op_flag = OPERATION;
      st_flag = 0;
    }
    else
      st_flag += 1;
  }
}
//ISR for CLK pin (determine which direction the encoder is rotating)
void CLK_ISR(void)
{
  static unsigned long lastInterruptTime = 0;
  unsigned long interruptTime = millis();

  // If interrupts come faster than 20ms, assume it's a bounce and ignore
  if (interruptTime - lastInterruptTime > 20) {
    if (Encoder_DT_value() == LOW)
    {
      Serial.println("Right Turn");
      if(st_flag==0 && op_flag==MODIFY)
        temp++;
      else if(st_flag==1)
        rpm++;
    }
    else {
      Serial.println("Left Turn");
      if(st_flag==0 && op_flag==MODIFY)
        temp--;
      else if(st_flag==1)
        rpm--;
    }
    //Updating lastinterrupt value
    lastInterruptTime = interruptTime;
    }
}

