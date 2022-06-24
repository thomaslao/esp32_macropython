from machine import Pin
from time import sleep

makerobo_Buzzer = 27    # 有源蜂鸣器管脚定义
timer=0.05

buzzer=Pin(makerobo_Buzzer,Pin.OUT)

buzzer.value(1)
while True:
    buzzer.value(0)     # 打开蜂鸣器控制
    sleep(timer)            # 延时时间
    buzzer.value(1)    # 关闭蜂鸣器控制
    sleep(timer)    
        
