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

print 'GHB mixieer'
scriptStarttime = time.time()
# time 2018-05-13 16:25:41.628000
chap_mxe = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/ghb/FeStage_mxy.ui
    ['D', (268, 1773), (84, 1589)],
    ['D', (811, 1768), (988, 1589)],
    ['END'],
    ['D', (84, 1589), (92, 1222)],
    ['D', (988, 1589), (988, 1409)],
    ['END'],
    ['D', (92, 1222), (92, 1050)],
    ['D', (445, 1773), (275, 1769)],
    ['END'],
    ['D', (988, 1409), (992, 1229)],
    ['D', (627, 1771), (627, 1575)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_mxe + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
