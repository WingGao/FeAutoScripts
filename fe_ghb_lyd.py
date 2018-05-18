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
    ['D', (269, 1578), (268, 1229)],
    ['D', (89, 1577), (89, 1231)],
    ['D', (269, 1761), (271, 1412)],
    ['END'],
    ['D', (268, 1229), (266, 1046)],
    ['END'],
    ['D', (89, 1231), (90, 1412)],
    ['D', (271, 1412), (94, 864)],
    ['D', (266, 1046), (278, 1229)],
    ['END'],
    ['D', (90, 1412), (276, 1229)],
    ['D', (271, 1041), (471, 829)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_lyd + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
