import bme280
import smbus2

# ======================================================================================================
# WeatherSensor class
# ======================================================================================================

class WeatherSensor():
    def __init__(self, port=1, address=0x77):
        self.port = port
        self.address = address
        self.bus = smbus2.SMBus(port)
        bme280.load_calibration_params(self.bus, self.address)

    def read(self):
        bme280_data = bme280.sample(self.bus, self.address)
        return bme280_data    