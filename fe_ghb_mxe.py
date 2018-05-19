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
    ['D', (268, 1773), (88, 1576)],
    ['D', (448, 1774), (264, 1578)],
    ['D', (624, 1769), (448, 1761)],
    ['D', (807, 1772), (266, 1760)],
    ['END'],
    ['D', (88, 1576), (92, 1223)],
    ['D', (264, 1578), (89, 1409)],
    ['D', (266, 1760), (91, 1588)],
    ['D', (448, 1761), (271, 1769)],
    ['END'],
    ['D', (92, 1223), (92, 1055)],
    ['END'],
    ['D', (271, 1769), (629, 1765)],
    ['D', (89, 1409), (276, 1591)],
    ['D', (91, 1588), (628, 1772)],
    ['END'],
    ['D', (276, 1591), (628, 1766)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_mxe + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
