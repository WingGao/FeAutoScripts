# coding=utf-8
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

import sys
import os

if ':' in os.path.abspath(__file__):  # windows
    sys.path.append(sys.path[0].split(':', 1)[1])
from utils import WingDevice
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
wd =WingDevice(device)
wd.test()
