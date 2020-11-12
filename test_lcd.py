from Adafruit_CharLCD import Adafruit_CharLCD
 
lcd = Adafruit_CharLCD(rs=21,en=20,d4=16,d5=12,d6=25,d7=24,cols=16,lines=2)
lcd.clear()
lcd.message("Hello\nworld")
