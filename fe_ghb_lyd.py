# coding=utf-8
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
import os

if ':' in os.path.abspath(__file__):  # windows
    # print sys.path
    sys.path.append(sys.path[0].split(':', 1)[1])

from utils import WingDevice
import time

# Connects to the current device, returning a MonkeyDevice object
print 'waitForConnection'
device = MonkeyRunner.waitForConnection()

print 'GHB luoyide'
scriptStarttime = time.time()
# time 2018-05-13 16:25:41.628000
chap_lyd = [
    # /Users/suamo/Projs/FeAutoScripts/FeLaya/laya/pages/ghb/FeStage_lyd.ui
    ['D', (272, 1592), (276, 1227)],
    ['D', (91, 1765), (272, 1407)],
    ['D', (93, 1586), (91, 1228)],
    ['D', (269, 1764), (275, 1590)],
    ['END'],
    ['D', (276, 1227), (452, 1048)],
    ['D', (272, 1407), (270, 1228)],
    ['D', (275, 1590), (271, 1404)],
    ['END'],
    ['D', (271, 1404), (827, 844)],
    ['D', (457, 858), (463, 634)],
    ['D', (270, 1228), (456, 1048)],
    ['D', (91, 1228), (93, 827)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_lyd + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
