#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：2.1.Water_LED.py
#  版本：V2.0
#  author: zhulin
# 说明：板载LED流水灯实验
#---------------------------------------
from machine import Pin
from utime import sleep
 
# 定义LED管脚
led=[16,17,18,19,23,5,1,3]
leds = [Pin(led[i],Pin.OUT) for i in range(0,8)]
 
 
# 程序入口
if __name__ == '__main__':
    # 循环语句
    while True:
        for n in range(0,8):# 依次点亮
            leds[n].value(1)
            sleep(0.05)
        for n in range(0,8): # 依次熄灭
            leds[n].value(0)
            sleep(0.05)