from machine import Timer,ADC,Pin,PWM,RTC

adc = machine.ADC(4)
PWM = PWM(Pin(15),freq=50)
conversion_factor = 3.3 / (65535)
rtc = RTC()

def do_thing(t):
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading-0.706) / 0.001721
    year,month,day,weekly,hours,minute,seconds,info =rtc.datetime()
    print(rtc.datetime())
    print(temperature)
    
def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    PWM.duty_u16(duty)
    
    print(f'可變電阻:{round(duty/65535*10)}')
    
t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)

