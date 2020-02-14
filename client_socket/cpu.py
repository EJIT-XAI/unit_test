import os
import string
import sys
import psutil
import time

cpuLimit = 0
memLimit = 0
serverName = "server1"
title = '[ '+ serverName +' ]\n'
msg = title

def getCpuUsage():
    cpu=0
    for x in range(2):
        cpu+=psutil.cpu_percent(interval=1)
        print(round(float(cpu)/3,2))

def getMemUsage():
    dmem = dict(psutil.Process().as_dict())

    limem = list(psutil.Process().as_dict().keys())
    print(dmem['memory_percent'])

getCpuUsage()
getMemUsage()
