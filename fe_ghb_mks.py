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

print 'GHB makusi'
scriptStarttime = time.time()
# time 2018-05-13 16:25:41.628000
chap_mks = [
    # D:\Projs\FeAutoScripts\FeLaya/laya/pages/ghb/FeStage_mks.ui
    ['D', (448, 1766), (448, 1582)],
    ['D', (815, 1765), (630, 1585)],
    ['D', (268, 1764), (447, 1768)],
    ['END'],
    ['D', (448, 1582), (452, 1233)],
    ['D', (447, 1768), (451, 1412)],
    ['D', (626, 1767), (449, 1594)],
    ['D', (630, 1585), (630, 1413)],
    ['END'],
    ['D', (452, 1233), (456, 1049)],
    ['D', (630, 1413), (450, 1405)],
    ['D', (632, 1408), (816, 1228)],
    ['T', (449, 1594), (636, 1227), (456, 1235)],
    ['END'],
    ['D', (635, 1411), (816, 1229)],
    ['D', (452, 1234), (275, 1234)],
    ['D', (636, 1227), (821, 1227)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_mks + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
