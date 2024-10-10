from machine import Pin
import time

red_led = Pin(15,Pin.OUT)
button = Pin(14,Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        red_led.toggle()# toggle 代表,暗變亮或亮變暗
        time.sleep(0.5)