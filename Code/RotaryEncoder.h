#ifndef ROTARYENCODER_H_
#define ROTARYENCODER_H_


#define OPERATION   0
#define MODIFY      1

#define RIGHT       0
#define LEFT        1
#define NONE        2

#define SW          3
#define DT          4
#define CLK         2

void Encoder_Init(void (*CallBackFuncSW)(void),void (*CallBackFuncCLK)(void));

#endif
