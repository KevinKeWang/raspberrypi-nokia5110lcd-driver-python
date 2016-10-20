# raspberrypi-nokia5110lcd-driver-python
# it's a python nokia5110 lcd driver use gpio.
# 用python实现5110显示屏驱动
<br/>
<b>how to start:</b><br/>
1. set gpio pin number in /Nokia5110/LCD.py <br/>
2. <br/>
  (1)if you want display cpu ram and ip of your raspberry. run this:<br/>
     python run.py<br/>
  (2)if you want display a string. run this:<br/>
     python run_print.py 'hello world!'<br/>
<br/>
<br/>
说明：<br/>
1.  在/Nokia5110/LCD.py文件中设置GPIO针脚<br/>
2. <br/>
    （1）如果你想显示cpu空闲、内存空闲、IP地址：<br/>
        python run.py<br/>
    （2）如果想输出一句话(仅支持英文)，直接执行：<br/>
        python run_print.py 'hello world!'<br/>
 
<img src="https://raw.githubusercontent.com/KevinKeWang/raspberrypi-nokia5110lcd-driver-python/master/IMG1.jpeg" alt="IMG1.jpeg">

<img src="https://raw.githubusercontent.com/KevinKeWang/raspberrypi-nokia5110lcd-driver-python/master/IMG2.jpeg" alt="IMG2.jpeg">
