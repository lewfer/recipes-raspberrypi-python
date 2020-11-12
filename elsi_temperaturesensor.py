from gpiozero import MCP3008

# ======================================================================================================
# TemperatureSensor class
# ======================================================================================================

class TemperatureSensor():
    """Temperature sensor class using the TMP36 sensor"""

    def __init__(self, mcp3008Pin):
        self.inp = MCP3008(mcp3008Pin)

    def read(self):
        value = self.inp.value
        millivolts = value * 3.3 * 1000 - 500  # -500 because the TMP36 has an offset of 500mV to allow for -ve temp readings
        temp = millivolts / 10                          # divide by 10 as 10mV per 1 degree C
        return temp
