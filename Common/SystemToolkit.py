# -*- coding=utf-8 -*-
import os
import re

# get system ip (mac or raspberrypi)
# 获取系统ip
def getIPs():
    result = []
    try:
        ipconfig = os.popen('ifconfig').readlines()
        if ipconfig:
            for l in ipconfig:
                ip = re.search(r'(inet addr:|inet\s)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', l)
                if ip and ip.group(2):
                    result.append(ip.group(2))
    except:
        result = []
    finally:
        return result


# get cpu idle (mac or raspberrypi)
# 获取cpuidle
def getCPUidle():
    if isMac():
        cmd = "top -l 1 |head -10|grep 'CPU usage'"
        strRe = r", (\d{1,2}\.\d{1,2}%) idle"
    else:
        cmd = "top -bn 1|head -5|grep '^%Cpu'"
        strRe = r",\s*(\d{1,2}\.\d{1,2})\s*id"

    result = ''
    try:
        cpu = os.popen(cmd).readline()
        # print cpu
        cpuidle = re.search(strRe, cpu)
        if cpuidle and cpuidle.group(1):
            result = cpuidle.group(1).strip()
    except:
        result = ''
    finally:
        return result


# get free memory size  (mac or raspberrypi)
# 获取内存空闲
def getMemFree():
    if isMac():
        cmd = "top -l 1 |head -10|grep 'PhysMem'"
        strRg = r",\s*(\d+(M|K|G))\s*unused."
    else:
        cmd = "top -bn 1|head -5|grep '^KiB Mem'"
        strRg = r",\s*(\d+)\s*free,"

    result = ''
    try:
        mem = os.popen(cmd).readline()
        # print mem
        memfree = re.search(strRg, mem)
        if memfree and memfree.group(1):
            result = memfree.group(1).strip()
    except:
        result = ''
    finally:
        return result


# get system type (mac or raspberrypi)
# 获取系统类型
def getSysType():
    uname = os.popen('uname -a').readline()
    if uname.startswith('Darwin'):
        return 'mac'
    else:
        return 'linux'

# get is this a mac or a raspberrypi
# 判断是否是Mac
def isMac():
    if getSysType() == 'mac':
        return True
    return False

# it's a test for this code file
# 测试
if __name__ == '__main__':
    print getIPs()
    print getCPUidle()
    print getMemFree()