from elsi_servobonnet import *

ServoBonnetFrequency(50)
s = ServoBonnet(0)

print('Moving servo, press Ctrl-C to quit...')
while True:
    s.angle(0)
    sleep(1)    
    s.angle(90)
    sleep(1)    
    s.angle(180)
    sleep(1)


