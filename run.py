#!/usr/bin/python
# -*- coding=utf-8 -*-
# the entry of this program

import sys
import os
import time
import re
import RPi.GPIO as GPIO
import Nokia5110
import Common


# off warnings
# 不提示GPIO占用警告
GPIO.setwarnings(False)

# initialization the gpio and lcd
# 初始化LCD
Nokia5110.init_gpio()
Nokia5110.init_lcd()

# main loop ,refresh data every 4 seconds
line = 0
while True:
    # clear lcd
    # 清屏
    Nokia5110.clear()

    # disply cpu idle
    # 显示cpu空闲
    cpuid = Common.getCPUidle()
    Nokia5110.write_english_string(0, line, "cpuid:" + cpuid)
    line += 1

    # disply memery free
    # 显示内存空闲
    memfr = Common.getMemFree()
    Nokia5110.write_english_string(0, line, "memfr:" + memfr)
    line += 1

    # get ipaddress from system and display them
    # 命令获取IP地址,逐行显示
    ips = Common.getIPs()
    print ips
    for ip in ips:
        Nokia5110.write_english_string(0, line, ip)
        line += 1

    # initialization line num, wait for 2 seconds
    line = 0
    time.sleep(2)

    # clear lcd . diskplay a bitmap . have fun.
    # 显示位图
    Nokia5110.clear()
    Nokia5110.draw_bmp_pixel(0, 0, Nokia5110.bmp_rock, 48, 48)
    time.sleep(2)


