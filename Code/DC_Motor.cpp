#include <Arduino.h>
#include "DC_Motor.h"

void Motor_Init(void)
{
  pinMode(DCM,OUTPUT);
}
void Motor_Rotate(int rpm)
{
  analogWrite(DCM,((rpm/MAX_RPM)*255.0));
}

