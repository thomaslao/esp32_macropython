#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：2.3.buzzer.py
#  版本：V2.0
#  author: zhulin
#  说明：有源蜂鸣器实验
#####################################################
from machine import Pin
from time import sleep

makerobo_Buzzer = 27    # 有源蜂鸣器管脚定义

# GPIO设置函数
def makerobo_setup(pin):
    global makerobo_BuzzerPin
    global buzzer
    makerobo_BuzzerPin = pin

    buzzer=Pin(makerobo_BuzzerPin,Pin.OUT)       # 设置有源蜂鸣器管脚为输出模式
    buzzer.value(1)                              # 蜂鸣器设置为高电平，关闭蜂鸟器

#  打开蜂鸣器
def makerobo_buzzer_on():
    buzzer.value(0)         # 蜂鸣器为低电平触发，所以使能蜂鸣器让其发声
# 关闭蜂鸣器
def makerobo_buzzer_off():
    buzzer.value(1)         # 蜂鸣器设置为高电平，关闭蜂鸟器

# 控制蜂鸣器鸣叫
def makerobo_beep(x):
    makerobo_buzzer_on()     # 打开蜂鸣器控制
    sleep(x)            # 延时时间
    makerobo_buzzer_off()    # 关闭蜂鸣器控制
    sleep(x)            # 延时时间

# 循环函数
def loop():
    while True:
        makerobo_beep(0.5) # 控制蜂鸣器鸣叫，延时时间为500mm

# 程序入口
if __name__ == '__main__':
    makerobo_setup(makerobo_Buzzer) # 设置GPIO管脚
    loop()                          # 调用循环函数

