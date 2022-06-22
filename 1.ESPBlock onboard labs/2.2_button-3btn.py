from machine import Pin
from time import sleep

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
        up_status=up_tmp
    
    #left
    left_status=left_button.value()
    if left_status != 1:
        print(state[1])
        
    #down
    down_tmp=down_button.value()
    if down_tmp!=down_status :
        print(state[2])
        down_status=down_tmp
    
    #right
    right_tmp=right_button.value()
    if right_tmp!=1:
        print(state[3])
        
    sleep(0.2)
    
    