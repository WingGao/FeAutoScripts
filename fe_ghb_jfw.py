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

print 'GHB jiefangwang'
scriptStarttime = time.time()
# time 2018-05-13 16:25:41.628000
chap_jfw = [
    # /Users/suamo/Projs/FeAutoScripts/FeLaya/laya/pages/ghb/FeStage_jfw.ui
    ['D', (630, 1587), (630, 1226)],
    ['D', (452, 1585), (631, 1409)],
    ['D', (815, 1586), (816, 1408)],
    ['D', (270, 1585), (629, 1592)],
    ['END'],
    ['D', (630, 1226), (449, 1226)],
    ['D', (631, 1409), (450, 1406)],
    ['D', (816, 1408), (631, 1411)],
    ['D', (629, 1592), (629, 1222)],
    ['END'],
    ['D', (450, 1406), (450, 1043)],
    ['D', (629, 1222), (624, 1045)],
    ['END'],
    ['D', (444, 1410), (450, 1049)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_jfw + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
