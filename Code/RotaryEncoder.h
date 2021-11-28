#ifndef ROTARYENCODER_H_
#define ROTARYENCODER_H_

//Modes of operation
#define OPERATION   0
#define MODIFY      1

//Encoder Pins
#define SW          3
#define DT          4
#define CLK         2

void Encoder_Init(void (*CallBackFuncSW)(void),void (*CallBackFuncCLK)(void));

#endif
