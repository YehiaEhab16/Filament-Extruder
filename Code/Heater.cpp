#include <Arduino.h>
#include "Heater.h"

void Heater_Init(void)
{
  pinMode(HEATER1,OUTPUT);
  pinMode(HEATER2,OUTPUT);
  pinMode(HEATER3,OUTPUT);
}
void Heater(int temp)
{
  analogWrite(HEATER1,((temp/MAX_TEMP)*255.0));
  analogWrite(HEATER2,((temp/MAX_TEMP)*255.0));
  analogWrite(HEATER3,((temp/MAX_TEMP)*255.0));
}

