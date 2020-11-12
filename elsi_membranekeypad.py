import RPi.GPIO as GPIO
from time import sleep

# ======================================================================================================
# Class MembraneKeypad
# ======================================================================================================

class MembraneKeypad():
    def __init__(self, rowPins, colPins):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Set up pin numbers        
        self.rowPins = rowPins
        self.colPins = colPins

        if len(self.colPins)==3:
            self.Matrix = [ 
                    ['1','2','3'],
                    ['4','5','6'],
                    ['7','8','9'],
                    ['*','0','#'] ]
        else:
            self.Matrix = [ 
                    ['1','2','3','A'],
                    ['4','5','6','B'],
                    ['7','8','9','C'],
                    ['*','0','#','D'] ]
                
    def __del__(self):
        '''Cleanup when the object is deleted'''
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup(self.rowPins)
        GPIO.cleanup(self.colPins)

    def initialise(self):
        '''Set up the pins ready to read a keypress'''
        # Initialise the column pins for output and output 0
        for col in range (len(self.colPins)):
                GPIO.setup(self.colPins[col], GPIO.OUT)
                GPIO.output(self.colPins[col], 0)

        # Initialise the row pins for input and pull up to 1
        for row in range(len(self.rowPins)):
                GPIO.setup(self.rowPins[row], GPIO.IN, pull_up_down = GPIO.PUD_UP)

    def cleanup(self):
        '''Cleanup after reading a keypress'''
        # Reinitialize all rows and columns as input 
        for i in range(len(self.rowPins)):
                GPIO.setup(self.rowPins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.colPins)):
                GPIO.setup(self.colPins[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        
    def getPress(self):
        '''Wait for a keypress'''
        self.initialise()
        while True:
            k = self.getPress2()
            if k is not None:
                sleep(0.1)      # delay to reduce repeat characters
                break
            sleep(0.01)
            #print(".", end="")
        self.cleanup()
        return k
            
    def getPress2(self):
        '''Check for a keypress - return None if no keypress or the character if there is one'''
        
        # Check if any row pressed - will be pulled down to 0
        rowVal = -1
        for i in range(len(self.rowPins)):
            if GPIO.input(self.rowPins[i]) == 0:
                rowVal = i
                
        # If no row pressed return
        if rowVal == -1:
            return None
        
        # Set columns as input now and pull down to 0
        for j in range(len(self.colPins)):
            GPIO.setup(self.colPins[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        # Set the pressed row to output and output 1
        GPIO.setup(self.rowPins[rowVal], GPIO.OUT)
        GPIO.output(self.rowPins[rowVal], GPIO.HIGH)

        # Check what col is pressed - will be pulled up to 1
        colVal = -1
        for j in range(len(self.colPins)):
            if GPIO.input(self.colPins[j]) == 1:
                colVal=j
                
        # If no col pressed return
        if colVal == -1:
            return None

        # Return the value of the key pressed
        return self.Matrix[rowVal][colVal]
    


