from gpiozero import MotionSensor

pir = MotionSensor(4)

print("Ready...")
while True:
    pir.wait_for_motion()
    print("Intruder!!")
    pir.wait_for_no_motion()
    print("Ready...")
