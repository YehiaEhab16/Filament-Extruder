#ifndef HEATER_H_
#define HEATER_H_

//Heaters pins
#define HEATER1     9
#define HEATER2     10
#define HEATER3     11

#define MAX_TEMP    400.0   //Max heater temperature

void Heater_Init(void);
void Heater(int temp);

#endif
