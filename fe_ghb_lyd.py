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
    ['D', (276, 1764), (276, 1411)],
    ['D', (274, 1583), (274, 1228)],
    ['D', (95, 1592), (91, 1228)],
    ['D', (97, 1763), (93, 1412)],
    ['END'],
    ['D', (274, 1228), (274, 1043)],
    ['D', (91, 1228), (271, 1228)],
    ['END'],
    ['D', (276, 1411), (92, 863)],
    ['T', (271, 1228), (91, 1043), (91, 862)],
    ['END'],
    ['D', (92, 1233), (286, 1043)],
    ['D', (466, 1043), (462, 859)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_lyd + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
