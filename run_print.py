#!/usr/bin/python
# -*- coding=utf-8 -*-
# the entry of this program

import sys
import RPi.GPIO as GPIO
import Nokia5110


# off warnings
# 不提示GPIO占用警告
GPIO.setwarnings(False)

# initialization the gpio and lcd
# 初始化LCD
Nokia5110.init_gpio()
Nokia5110.init_lcd()

# get string
str = 'hello world'
if len(sys.argv)>1:
    str=sys.argv[1]

# print string
Nokia5110.write_english_string(0, 0, str)


