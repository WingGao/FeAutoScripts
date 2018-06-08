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
    ['D', (89, 1595), (93, 1232)],
    ['D', (272, 1592), (268, 1233)],
    ['D', (266, 1765), (274, 1419)],
    ['D', (88, 1767), (271, 1591)],
    ['END'],
    ['D', (268, 1233), (453, 1043)],
    ['D', (274, 1419), (278, 1238)],
    ['D', (271, 1591), (275, 1410)],
    ['END'],
    ['D', (93, 1232), (97, 843)],
    ['D', (453, 863), (824, 847)],
    ['T', (275, 1410), (453, 1227), (449, 1036)],
    ['D', (278, 1238), (450, 1034)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_lyd + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
