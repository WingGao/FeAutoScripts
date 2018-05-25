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
    ['D', (272, 1592), (264, 1230)],
    ['D', (91, 1765), (91, 1409)],
    ['D', (93, 1586), (89, 1227)],
    ['D', (269, 1764), (273, 1590)],
    ['END'],
    ['D', (273, 1590), (273, 1227)],
    ['D', (264, 1230), (450, 1036)],
    ['D', (91, 1409), (272, 1226)],
    ['END'],
    ['D', (269, 1407), (277, 1225)],
    ['D', (450, 860), (458, 1040)],
    ['D', (89, 1227), (85, 846)],
    ['D', (272, 1226), (276, 1038)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_lyd + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
