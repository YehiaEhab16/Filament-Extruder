#include <Arduino.h>
#include "RotaryEncoder.h"

void Encoder_Init(void (*CallBackFuncSW)(void),void (*CallBackFuncCLK)(void))
{
  pinMode(CLK, INPUT_PULLUP);
  pinMode(DT, INPUT_PULLUP);
  pinMode(SW, INPUT_PULLUP);

  Serial.begin(9600);
  Serial.println("Initializing code ...");
  Serial.println("******************************");
  attachInterrupt(digitalPinToInterrupt(SW), CallBackFuncSW, FALLING);
  attachInterrupt(digitalPinToInterrupt(CLK), CallBackFuncCLK, FALLING);
}

