
from machine import Pin
from utime import sleep

while True:    # 循环语句
    led1=Pin(16,Pin.OUT)
    led2=Pin(17,Pin.OUT)
    led1.value(1)
    led2.value(0)
    sleep(0.2)
    led1.value(0)
    led2.value(1)
    sleep(0.2)
