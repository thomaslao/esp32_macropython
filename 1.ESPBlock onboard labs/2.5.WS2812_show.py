#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：2.5.WS2812_show.py
#  版本：V2.0
#  author: zhulin
# 说明：RGBS彩灯实验
#####################################################
import time
import machine, neopixel

numpix = 4
p = 16
strip = neopixel.NeoPixel(machine.Pin(p), numpix)

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (138, 43, 226)
COLORS = (RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET)

while True:
    for color in COLORS:
        for i in range(numpix):
            strip[i]=(color[0], color[1], color[2])
            time.sleep(0.1)
            strip.write()
