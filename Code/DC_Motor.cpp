#include <Arduino.h>
#include "DC_Motor.h"

//Initialize motor pin as output
void Motor_Init(void)
{
  pinMode(DCM,OUTPUT);
}

//Output volatge according to input RPM
void Motor_Rotate(int rpm)
{
  analogWrite(DCM,((rpm/MAX_RPM)*255.0));
}

