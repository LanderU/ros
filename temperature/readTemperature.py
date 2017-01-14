#!/usr/bin/env python

import spidev
from MPU9250 import MPU9250
import commands
import time

res = commands.getstatusoutput('whoami')

if res [1] == 'root':
	# Initialize the driver
	imu = MPU9250()
	imu.initialize()
	# Read Temperature
	while True:
		print "{00:.2f}".format(imu.read_temp())
		time.sleep(3)
else:
	print 'Execute this script with \"sudo\"'
