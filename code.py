import usb_hid
import time
from adafruit_hid.mouse import Mouse
import board
from digitalio import DigitalInOut, Direction, Pull

moveDistance = 300
moveSpace = 5
delaySec = 0.01

led = DigitalInOut(board.GP25)
led.direction = Direction.OUTPUT

btn = DigitalInOut(board.GP17)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

mouse = Mouse(usb_hid.devices)
switch = False

def isButtonPressed():
    if(btn.value == True):
        while btn.value:
            1
        return True
    return False


led.value = True
time.sleep(0.1)
led.value = False
time.sleep(0.1)
led.value = True
time.sleep(0.1)
led.value = False
time.sleep(0.1)
led.value = True
time.sleep(0.1)
led.value = False

while True:
    if(isButtonPressed() == True):
        switch = not switch
        
    if (switch == True):
        led.value = 1
        for xAxis in range(0, moveDistance, moveSpace):
            mouse.move(x=moveSpace)
            time.sleep(delaySec)
        for xAxis in range(0, moveDistance, moveSpace):
            mouse.move(x=-moveSpace)
            time.sleep(delaySec)
    else:
        led.value = 0
    
    time.sleep(delaySec)
