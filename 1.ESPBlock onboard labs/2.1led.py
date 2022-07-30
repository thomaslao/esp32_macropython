from machine import Pin
from utime import sleep

led=Pin(16,Pin.OUT)
while True:
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)
