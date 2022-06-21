#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：2.2_button.py
#  版本：V2.0
#  author: zhulin
# 说明：板载方向按键实验
#---------------------------------------
from machine import Pin
from time import sleep

makerobo_upPin = 22    #轻触按键Pin端口
makerobo_leftPin = 32  #轻触按键Pin端口
makerobo_downPin = 25  #轻触按键Pin端口
makerobo_rightPin = 26 #轻触按键Pin端口

up_button = Pin(makerobo_upPin, Pin.IN, Pin.PULL_UP)       # 设置up_button管脚为输入模式，上拉至高电平(3.3V)
left_button = Pin(makerobo_leftPin, Pin.IN, Pin.PULL_UP)   # 设置left_button管脚为输入模式，上拉至高电平(3.3V)
down_button = Pin(makerobo_downPin, Pin.IN, Pin.PULL_UP)   # 设置down_button管脚为输入模式，上拉至高电平(3.3V)
right_button = Pin(makerobo_rightPin, Pin.IN, Pin.PULL_UP) # 设置right_button管脚为输入模式，上拉至高电平(3.3V)

state = ['up', 'left','down', 'right']  # 方向状态信息

makerobo_up_status = 1
makerobo_left_status = 1
makerobo_down_status = 1
makerobo_right_status = 1
while True:
    # up
    makerobo_up_tmp = up_button.value()
    if makerobo_up_tmp != makerobo_up_status:
        if makerobo_up_tmp == 0:
            print(state[0])
        makerobo_up_status = makerobo_up_tmp

    # left
    makerobo_left_tmp = left_button.value()
    if makerobo_left_tmp != makerobo_left_status:
        if makerobo_left_tmp == 0:
            print(state[1])
        makerobo_left_status = makerobo_left_tmp

    # down
    makerobo_down_tmp = down_button.value()
    if makerobo_down_tmp != makerobo_down_status:
        if makerobo_down_tmp == 0:
            print(state[2])
        makerobo_down_status = makerobo_down_tmp

    # right
    makerobo_right_tmp = right_button.value()
    if makerobo_right_tmp != makerobo_right_status:
        if makerobo_right_tmp == 0:
            print(state[3])
        makerobo_right_status = makerobo_right_tmp

    sleep(0.02)
