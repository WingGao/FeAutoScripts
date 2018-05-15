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

# 10连
# 罗伊-近防3 迪幽特-生命2 温蒂-防大1 希玛-防守指挥1
#

print 'GHB nabeer'
scriptStarttime = time.time()
# time 2018-05-13 16:25:41.628000
chap_nbe = [
    # /Users/suamo/Projs/FeAutoScripts/FeLaya/laya/pages/ghb/FeStage_nbe.ui
    ['D', (452, 1405), (640, 1400)],
    ['D', (266, 1588), (632, 1590)],
    ['END'],
    ['D', (268, 1405), (451, 1408)],
    ['END'],
    ['D', (632, 1590), (817, 1401)],
    ['D', (449, 1586), (631, 1593)],
    ['D', (640, 1400), (628, 1052)],
    ['END'],
    ['D', (451, 1408), (452, 1224)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_nbe + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
