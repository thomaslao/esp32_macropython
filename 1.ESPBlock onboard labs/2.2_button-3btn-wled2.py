from machine import Pin
from time import sleep

# 定义LED管脚
led1_pin=16
led2_pin=17
led3_pin=18
led4_pin=19
led1 = Pin(led1_pin,Pin.OUT)
led2 = Pin(led2_pin,Pin.OUT)
led3 = Pin(led3_pin,Pin.OUT)
led4 = Pin(led4_pin,Pin.OUT)
 
uppin=22
leftpin=32
downpin=25
rightpin=26

up_button=Pin(uppin,Pin.IN,Pin.PULL_UP)
left_button=Pin(leftpin,Pin.IN,Pin.PULL_UP)
down_button=Pin(downpin,Pin.IN,Pin.PULL_UP)
right_button=Pin(rightpin,Pin.IN,Pin.PULL_UP)

state=['up','left','down','right']

up_status=1
left_status=1
down_status=1
right_status=1

while True:
    up_tmp=up_button.value()
    if up_tmp!=up_status:
        if up_tmp==0:
            print(state[0])
            led1.value(1)
            sleep(0.1)
            led1.value(0)
        up_status=up_tmp
    
    #left
    left_status=left_button.value()
    if left_status != 1:
        print(state[1])
        led2.value(1)
        sleep(0.1)
        led2.value(0)
        
    #down
    down_tmp=down_button.value()
    if down_tmp!=down_status :
        print(state[2])
        led3.value(1)
        sleep(0.1)
        led3.value(0)
        down_status=down_tmp
    
    #right
    right_tmp=right_button.value()
    if right_tmp!=right_status:
        if right_tmp==0:
            print(state[3])
            led4.value(1)
            sleep(0.1)
            led4.value(0)
        right_status=up_tmp
    sleep(0.1)
    
    