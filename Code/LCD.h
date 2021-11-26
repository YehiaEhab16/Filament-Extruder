#ifndef LCD_H_
#define LCD_H_

#define WELCOME_DELAY     3000

void LCD_Init(void);
void LCD_Display(const String string);
void LCD_DisplayExactPosition(const String string,int x,int y);

#endif
