print(" ----------------------------------main.py---------------------------------- ")
import time
from machine import Pin


led = Pin(2, Pin.OUT)

while True:
    led.on() # led.value(1)
    print("LED on")
    time.sleep(1)
    led.off() # led.value(0)
    print("LED off")
    time.sleep(1)
