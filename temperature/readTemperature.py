#!/usr/bin/env python

import sys
try:
        import spidev
except ImportError:
        print 'sudo apt-get install python-spidev'
        sys.exit(0)
from MPU9250 import MPU9250
import commands
from time import sleep

res = commands.getstatusoutput('whoami')

if res [1] == 'root':
        # Initialize the driver
        imu = MPU9250()
        imu.initialize()
        # Read Temperature
        while True:
                print "{00:.2f}".format(imu.read_temp())
                sleep(3)
else:
        print 'Execute this script with \"sudo\"'