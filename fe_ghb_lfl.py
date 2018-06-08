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
    ['D', (88, 867), (270, 1053)],
    ['D', (98, 1215), (92, 1051)],
    ['D', (95, 1409), (89, 1228)],
    ['D', (89, 680), (91, 872)],
    ['END'],
    ['D', (270, 1053), (459, 1056)],
    ['D', (92, 1051), (278, 1057)],
    ['D', (91, 872), (90, 1049)],
    ['END'],
    ['D', (90, 1049), (456, 876)],
    ['D', (278, 1057), (645, 1218)],
    ['END'],
    # ['STAGE'],
]


end = [
    ['EXIT']
]

allstep = chap_lfl + end

wd = WingDevice(device)
wd.loop_ghb(allstep)  # 134场
