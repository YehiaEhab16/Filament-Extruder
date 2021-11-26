#ifndef DC_MOTOR_H_
#define DC_MOTOR_H_

#define DCM         6

#define MAX_RPM     200.0

void Motor_Init(void);
void Motor_Rotate(int rpm);

#endif
