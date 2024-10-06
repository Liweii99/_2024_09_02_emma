from machine import Pin
import time
led = Pin("LED",mode=Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
