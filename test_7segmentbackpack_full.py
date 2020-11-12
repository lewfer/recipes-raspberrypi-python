from elsi_sevensegment import *

# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()

# Initialize the display. Must be called once before using the display.
display.begin()

# Display a floating point number
display.clear()
display.print_float(23.45)
display.write_display()
sleep(3.0)

# Left justify
display.clear()
display.print_float(4.56, justify_right=False)
display.write_display()
sleep(3.0)

# Display a hex number
display.clear()
display.print_hex(0xfd)
display.write_display()
sleep(3.0)

# Display an inverted number
display.set_invert(True)
display.clear()
display.print_float(23.45)
display.write_display()
sleep(3.0)
display.set_invert(False)

# Display a single digit
display.clear()
display.set_digit(2, 4, decimal=True)
display.write_display()
sleep(3.0)

# Display the colon
display.clear()
display.set_colon(True)
display.write_display()
sleep(3.0)

# Display a decimal point
display.clear()
display.set_decimal(3, True)
display.write_display()
sleep(3.0)

# Display a string number
display.clear()
display.print_number_str("876", justify_right=False)
display.write_display()
sleep(3.0)

# Display raw segments
display.clear()
display.set_digit_raw(0, bitmask=0x44)
display.set_digit_raw(1, bitmask=0x6f)
display.set_digit_raw(2, bitmask=0xbb)
display.set_digit_raw(3, bitmask=0x20)
display.write_display()
sleep(3.0)

