# coding=utf-8
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

import sys
import os

if ':' in os.path.abspath(__file__):  # windows
    sys.path.append(sys.path[0].split(':', 1)[1])
from utils import WingDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
wd = WingDevice(device, debug=True)
# wd.test()
# wd.get_ok_btn()

chap_test = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/ghb/FeStage_test.ui
    ['D', (449, 903), (273, 544)],
    ['D', (273, 729), (452, 902)],
    ['END'],
    ['D', (273, 544), (454, 907)],
    ['D', (97, 914), (272, 906)],
    ['RESET'],
    ['D', (276, 904), (276, 543)],
    ['END'],
    ['STAGE'],
]

wd.startFe(chap_test, False)


def test_task_ok():
    pass
