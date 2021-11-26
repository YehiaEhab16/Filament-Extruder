#include <Arduino.h>
#include "LCD.h"

#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display

void LCD_Init(void)
{
  lcd.init();
  lcd.backlight();
  lcd.setCursor(3,0);
  lcd.print("Welcome to");
  lcd.setCursor(4,1);
  lcd.print("Extruder");
  delay(WELCOME_DELAY);
  lcd.clear();
  lcd.print("Temp:");
  lcd.setCursor(0,1);
  lcd.print("RPM:");
}
void LCD_DisplayExactPosition(const String string,int x,int y)
{
  lcd.setCursor(x,y);
  lcd.print(string);
}
void LCD_Display(const String string)
{
  lcd.print(string);
}

