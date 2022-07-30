from machine import Pin
from time import sleep

# 定义LED管脚
led=[0,16,17,18,19,23,5,1,3]
leds = [Pin(led[i],Pin.OUT) for i in range(1,9)]
 
uppin=22
leftpin=32
downpin=25
rightpin=4

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
            leds[1].value(1)
            sleep(0.1)
            leds[1].value(0)
        up_status=up_tmp
    
    #left
    left_status=left_button.value()
    if left_status != 1:
        print(state[1])
        leds[2].value(1)
        sleep(0.1)
        leds[2].value(0)
        
    #down
    down_tmp=down_button.value()
    if down_tmp!=down_status :
        print(state[2])
        leds[3].value(1)
        sleep(0.1)
        leds[3].value(0)
        down_status=down_tmp
    
    #right
    right_tmp=right_button.value()
    if right_tmp!=1:
        print(state[3])
        leds[4].value(1)
        sleep(0.1)
        leds[4].value(0)
        
    sleep(0.5)
    
    