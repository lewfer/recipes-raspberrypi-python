import RPi.GPIO as GPIO
from time import sleep
from time import ctime

# ======================================================================================================
# SevenSegment class
# ======================================================================================================

class SevenSegmentRaw():
    def __init__(self, digitPins, segmentPins, colonPin, commonAnode=True):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.digitPins = digitPins
        self.segmentPins = segmentPins
        self.colonPin = colonPin

        if commonAnode:
            self.SEGON = 0
            self.SEGOFF = 1
            self.DIGON = 1
            self.DIGOFF = 0
        else:
            self.SEGON = 1
            self.SEGOFF = 0
            self.DIGON = 0
            self.DIGOFF = 1   

        # Turn all digits off
        for digit in self.digitPins:
            GPIO.setup(digit, GPIO.OUT)
            GPIO.output(digit, self.DIGOFF)

        # Turn all segments off
        for segment in self.segmentPins:
            GPIO.setup(segment, GPIO.OUT)
            GPIO.output(segment, self.SEGOFF)

        # Colon pin off
        GPIO.setup(colonPin, GPIO.OUT)
        GPIO.output(colonPin, self.SEGOFF)            
        
        OFF = self.SEGOFF
        ON = self.SEGON
        self.nums = {
            ' ':(OFF,OFF,OFF,OFF,OFF,OFF,OFF),
            '0':(ON ,ON ,ON ,OFF,ON ,ON ,ON ),
            '1':(OFF,OFF,ON ,OFF,OFF,ON ,OFF),
            '2':(ON ,OFF,ON ,ON ,ON ,OFF,ON ),
            '3':(ON ,OFF,ON ,ON ,OFF,ON ,ON ),
            '4':(OFF,ON ,ON ,ON ,OFF,ON ,OFF),
            '5':(ON ,ON ,OFF,ON ,OFF,ON ,ON ),
            '6':(ON ,ON ,OFF,ON ,ON ,ON ,ON ),
            '7':(ON ,OFF,ON ,OFF,OFF,ON ,OFF),
            '8':(ON ,ON ,ON ,ON ,ON ,ON ,ON ),
            '9':(ON ,ON ,ON ,ON ,OFF,ON ,ON )}
           
    def display(self, digits, dots, colon):
        # For each digit
        for digit in range(4):
            # Dispay the 7-segment number
            for segment in range(0,7):
                GPIO.output(self.segmentPins[segment], self.nums[digits[digit]][segment])

            # Display the dot if requested
            GPIO.output(self.segmentPins[7], self.SEGON if dots[digit]=="." else self.SEGOFF)

            # Display the : if requested
            GPIO.output(self.colonPin, self.SEGON if colon else self.SEGOFF)

            # Turn on the digit for 1 millisecond
            GPIO.output(self.digitPins[digit], self.DIGON)
            sleep(0.001)
            GPIO.output(self.digitPins[digit], self.DIGOFF)     

    def displayTime(self):
        while True:
            digits = ctime()[11:13]+ctime()[14:16]   # get the time
            self.display(digits, "    ", True)    

    def displayDigits(self, digits, dots="    "):
        while True:
            self.display(digits, dots, False) 


seg = SevenSegmentRaw(digitPins=(21, 20, 16, 12), segmentPins=(26,19,13,6,5,11,9,10), colonPin=22)
try:
    #seg.displayTime()
    seg.displayDigits("3456")
except KeyboardInterrupt:
  GPIO.cleanup()    