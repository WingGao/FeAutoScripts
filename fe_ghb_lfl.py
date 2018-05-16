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

print 'GHB lufulai'
scriptStarttime = time.time()
# time 2018-05-13 16:25:41.628000
chap_lfl = [
    # /Users/suamo/Projs/FeAutoScripts/FeLaya/laya/pages/ghb/FeStage_lfl.ui
    ['D', (88, 869), (265, 1055)],
    ['D', (91, 1228), (271, 1057), 1],
    ['END'],
    ['D', (92, 681), (454, 870)],
    ['D', (455, 1065), (451, 867)],
    ['D', (88, 1061), (457, 1063)],
    ['END'],
    ['D', (457, 1063), (457, 1222)],
    ['END'],
    # ['STAGE'],
]


end = [
    ['EXIT']
]

allstep = chap_lfl + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
