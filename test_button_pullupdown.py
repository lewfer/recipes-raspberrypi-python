from elsi_raw_library import *

bpullup = RawButtonPullup(21)
bpulldown = RawButtonPulldown(20)

while True:
    print("Pullup on 21:", bpullup.value(), "Pulldown on 20:", bpulldown.value())
    sleep(0.1)