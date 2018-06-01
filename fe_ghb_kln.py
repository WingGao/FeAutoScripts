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
    ['D', (630, 1586), (446, 1408)],
    ['D', (992, 1405), (812, 1409), 2],
    ['D', (450, 1406), (450, 1040)],
    ['END'],
    ['T', (447, 1220), (267, 1229), (267, 1046)],
    ['D', (631, 1593), (456, 1592)],
    ['END'],
    ['D', (992, 1406), (992, 878)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap_kln + end

wd = WingDevice(device)
wd.loop_ghb(allstep)
