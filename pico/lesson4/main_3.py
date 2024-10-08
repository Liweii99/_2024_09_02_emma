from machine import Timer, Pin

#tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
#tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print(2))
green_led = Pin("LED",Pin.OUT)
green_count = 0
def green_led_mycallback(t:Timer):
    global green_count #全域,外部
    green_count += 1
    #print(f"目前mycallback被執行:{count}次")
    green_led.toggle()
    print("green_led初執行")
    if green_count >= 10:
        t.deinit()

green_led_timer =Timer(period = 1000,mode=Timer.PERIODIC,callback=green_led_mycallback)

red_count = 0
def red_led_mycallback(t:Timer):
    global red_count #全域,外部
    red_count = red_count + 1
    #print(f"目前mycallback被執行:{count}次")
    #green_led.toggle()
    print ("red_led初執行")
    if red_count >= 10:
        t.deinit()
red_led_timer = Timer(period=2000,mode=Timer.PERIODIC,callback=red_led_mycallback)
