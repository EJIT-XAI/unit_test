# !/bin/python

import os
import string
import sys
import psutil
import time



cpuLimit = 0
memLimit = 0
serverName= "server1"
title = '[' + serverName + ' ]\n'
msg = title

def getCpuUsage():
	cpu=0
	for x in range(2):
		cpu+=psutil.cpu_percent(interval=1)
	return round(float(cpu)/3,2)

def getMemUsage():
	mem=str(os.popen('free -t -m').readlines())
	T_ind=mem.index('T')
	mem=mem[T_ind+6:]
	mem_T=mem[:13]
	mem_sub=mem[14:]
	mem_U=mem_sub[:13]
	return round(float(mem_U)/float(mem_T)*100,2)

avgCpu = getCpuUsage()
memUsage = getMemUsage()

if avgCpu > cpuLimit:
	msg += 'cpu usage exceeded ' + str(cpuLimit) + '% \n'
	msg += 'cpu usage : '+str(avgCpu) + '%\n'
if memUsage > memLimit:
	msg += 'memory usage exceeded ' + str(memLimit) + '% \n'
	msg += 'memory usage : ' + str(memUsage) + '% \n'
if avgCpu > cpuLimit or memUsage > memLimit:
	msg += serverName + 'is doing something'
	print(msg)
	os.system('need to start with root auth in commendline')
	time.sleep(5)
	msg= title + 'restarted and cpu & memory is like this\n'
	msg += 'cpu usage : ' + str(getCpuUsage()) + '%\n'
	msg += 'memory usage : ' + str(getMemUsage()) + '%n'
	print(msg)
print(msg)
