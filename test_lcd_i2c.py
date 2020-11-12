import RPi_I2C_driver
from time import sleep

lcd = RPi_I2C_driver.lcd()
lcd.lcd_display_string("Hello", 1)
lcd.lcd_display_string("World", 2)

sleep(2)
lcd.lcd_clear()