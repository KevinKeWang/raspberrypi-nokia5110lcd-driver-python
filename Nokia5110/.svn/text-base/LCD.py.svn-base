# -*- coding=utf-8 -*-
# it's all the functions of control lcd or print something.
# 所有控制LCD和打印字符/图像的方法都在这里

import Toolkit
import Font6x8
import RPi.GPIO as GPIO

SCLK = 37
SDIN = 35
LCD_DC = 33
LCD_CE = 31
LCD_RST = 29


# 初始化GPIO
def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SCLK, GPIO.OUT)
    GPIO.setup(SDIN, GPIO.OUT)
    GPIO.setup(LCD_DC, GPIO.OUT)
    GPIO.setup(LCD_CE, GPIO.OUT)
    GPIO.setup(LCD_RST, GPIO.OUT)


# LCD初始化
def init_lcd():
    # 产生一个让LCD复位的低电平脉冲
    GPIO.output(LCD_RST, GPIO.LOW)
    Toolkit.delay_1us()
    GPIO.output(LCD_RST, GPIO.HIGH)

    # 关闭LCD
    GPIO.output(LCD_CE, GPIO.LOW)
    Toolkit.delay_1us()

    # 使能LCD
    GPIO.output(LCD_CE, GPIO.HIGH)
    Toolkit.delay_1us()

    write_byte(0x21, 0)  # 使用扩展命令设置LCD模式
    write_byte(0xa0, 0)  # 设置偏置电压
    write_byte(0x07, 0)  # 温度校正
    write_byte(0x17, 0)  # 1:48
    write_byte(0x20, 0)  # 使用基本命令
    clear()  # 清屏
    write_byte(0x0c, 0)  # 设定显示模式，正常显示

    # 关闭LCD
    GPIO.output(LCD_CE, GPIO.LOW)


# LCD清屏函數
def clear():
    write_byte(0x0c, 0)
    write_byte(0x80, 0)

    i = 0
    while i < 504:
        write_byte(0, 1)
        i += 1


# 输出字符串
def write_english_string(x, y, str):
    set_xy(x, y)
    for c in str:
        write_char(c)


# 输出一个字符
def write_char(c):
    # 编码表与索引值相差32
    idx = ord(c) - 32

    # 逐列输出点阵
    line = 0
    while line < 6:
        write_byte(Font6x8.fonts_6x8[idx][line], 1)
        line += 1


# 绘制位图  X、Y：位图绘制的起始X、Y坐标；   map：位图点阵数据；     pix_x：位图像素（长）；  pix_y：位图像素（宽）
def draw_bmp_pixel(x, y, map, pix_x, pix_y):
    # 计算位图所占行数
    if pix_y % 8 == 0:
        row = pix_y // 8
    else:
        row = pix_y / 8 + 1

    # 逐行输出数据，一次输出一个字节
    n = 0
    while n < row:  # 遍历行
        set_xy(x, y)  # 设置行起点
        i = 0
        while i < pix_x:  # 遍历列
            write_byte(map[i + n * pix_x], 1)  # 写入一字节数据
            i += 1
        y += 1  # 增加行号
        n += 1


# 写入一个字节命令或数据 参数：data：写入值 command:0-命令 1-数据
def write_byte(data, command):
    GPIO.output(LCD_CE, GPIO.LOW)

    # 判断是否是命令，设置标志位
    if command == 0:
        # 传命令
        GPIO.output(LCD_DC, GPIO.LOW)
    else:
        # 传数据
        GPIO.output(LCD_DC, GPIO.HIGH)

    # 按位输出数据或命令
    i = 0
    while i < 8:
        # 取最高位数据（从高位到低位的顺序输出）
        if data & 0x80 > 0:
            GPIO.output(SDIN, GPIO.HIGH)
        else:
            GPIO.output(SDIN, GPIO.LOW)

        # 时钟信号从低到高跳变（上升沿触发）
        GPIO.output(SCLK, GPIO.LOW)
        data <<= 1;  # 数据按位向左移一位
        GPIO.output(SCLK, GPIO.HIGH)

        i += 1

    GPIO.output(LCD_CE, GPIO.HIGH)


# 设置坐标 输入参数：X：0－83；Y：0－5
def set_xy(x, y):
    write_byte(0x40 | y, 0)  # column
    write_byte(0x80 | x, 0)  # row
