'''
from machine import Pin
led = Pin("LED",Pin.OUT)
led.value(0)
'''
'''
from machine import Pin
led = Pin("LED",Pin.OUT)
led.on()
 '''
'''
from machine import Pin
led = Pin("LED",Pin.OUT)
led.off()
'''
'''
from machine import Pin
led = Pin("LED",Pin.OUT)
while True:
    led.on()
'''
'''
from machine import Pin
import time
    
led = Pin("LED",Pin.OUT)

while True:
    led.on()
    print ("Hello!")
    time.sleep(1)
 '''   
    
from machine import Pin
import time
    
led = Pin("LED",Pin.OUT)
status = False
while True:
    led.on()
    if status == False:
        led.on()
        status = True
    else:
        led.off()
        status = False
    time.sleep(1)    
    
    
    
    
    