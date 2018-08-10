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

print 'GHB kelainie'
scriptStarttime = time.time()
# time 2018-05-13 16:25:41.628000
chap_kln = [
    # /Users/suamo/Projs/FeAutoScripts/FeLaya/laya/pages/ghb/FeStage_kln.ui
    ['D', (811, 1402), (447, 1406)],
    ['D', (630, 1586), (630, 1413), 1],
    ['D', (633, 1406), (448, 1040)],
    ['END'],
    ['T', (452, 1218), (448, 1035), (262, 1035)],
    ['T', (812, 1590), (634, 1413), (628, 1046)],
    # ['D', (630, 1591), (630, 1041)],
    # ['D', (812, 1590), (816, 1413)],
    ['END'],
    ['D', (446, 1043), (627, 1043)],
    ['D', (634, 1415), (626, 1041)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_kln + end

wd = WingDevice(device, debug=False)
wd.loop_ghb(allstep)
