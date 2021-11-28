#include <Arduino.h>
#include "RotaryEncoder.h"

//Initializing Pins as input pullup and CLK,SW pins as interrupts
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

