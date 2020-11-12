from Adafruit_LED_Backpack import SevenSegment
from time import sleep

display = SevenSegment.SevenSegment()
display.begin()

# Display a floating point number
display.clear()
display.print_number_str(str(1.234))
display.write_display()
sleep(3.0)
display.print_number_str(str(23.45))
display.write_display()
sleep(3.0)
display.print_number_str(str(345.6))
display.write_display()
sleep(3.0)