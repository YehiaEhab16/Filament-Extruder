#ifndef DC_MOTOR_H_
#define DC_MOTOR_H_

#define DCM         6       //PWM pin for motor

#define MAX_RPM     200.0   //Max motor RPM

void Motor_Init(void);
void Motor_Rotate(int rpm);

#endif
