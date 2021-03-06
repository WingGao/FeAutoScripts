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

print 'Chap1-2 10连'
scriptStarttime = time.time()

# time 2018-04-28 12:27:34.713615
chap01 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage01.ui
    ['PREPARE'],
    ['D', (274, 1046), (91, 1049)],
    ['D', (92, 1234), (271, 1228)],
    ['PREPARE'],
    ['D', (91, 1049), (814, 1043)],
    ['D', (271, 1228), (446, 1225)],
    ['D', (277, 1050), (271, 1236)],
    ['D', (92, 1233), (268, 1048)],
    ['END'],
    ['D', (448, 1040), (817, 1037)],
    ['END'],
    ['T', (446, 1225), (626, 1243), (626, 1057)],
    ['END'],
    ['STAGE'],
]
chap02 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage02.ui
    ['D', (808, 1409), (804, 1593)],
    ['T', (812, 1046), (811, 682), (632, 688)],
    ['D', (996, 1231), (986, 1419)],
    ['END'],
    ['D', (804, 1593), (645, 1614)],
    ['END'],
    ['D', (805, 1587), (642, 1603)],
    ['D', (986, 1419), (641, 1604)],
    ['END'],
    ['STAGE'],
]
chap03 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage03.ui
    ['PREPARE'],
    ['D', (450, 1593), (632, 1583)],
    ['D', (633, 1767), (454, 1759)],
    ['PREPARE'],
    ['D', (632, 1583), (632, 1221)],
    ['D', (456, 1584), (456, 1223)],
    ['D', (455, 1767), (461, 1406)],
    ['D', (634, 1765), (635, 1575)],
    ['END'],
    ['D', (456, 1223), (448, 877)],
    ['D', (632, 1221), (632, 873)],
    ['D', (461, 1406), (451, 695)],
    ['END'],
    ['STAGE'],
]
chap04 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage04.ui
    ['D', (451, 1773), (267, 1773)],
    ['D', (630, 1590), (458, 1762)],
    ['D', (989, 1582), (627, 1589)],
    ['D', (814, 1769), (804, 1585)],
    ['END'],
    ['D', (267, 1773), (267, 1585)],
    ['D', (627, 1589), (451, 1578)],
    ['D', (804, 1585), (632, 1589)],
    ['END'],
    ['D', (267, 1585), (89, 1579)],
    ['END'],
    ['D', (632, 1589), (815, 1218)],
    ['D', (89, 1579), (91, 1400)],
    ['END'],
    ['D', (88, 1577), (101, 1229)],
    ['D', (451, 1578), (101, 1234)],
    ['END'],
    ['STAGE'],
]
chap05 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage05.ui
    ['D', (807, 507), (617, 693)],
    ['END'],
    ['D', (617, 693), (275, 689)],
    ['END'],
    ['D', (275, 689), (275, 871)],
    ['D', (811, 687), (815, 506)],
    ['D', (985, 871), (982, 510)],
    ['D', (989, 690), (992, 867)],
    ['END'],
    ['D', (275, 871), (293, 1263)],
    ['D', (992, 867), (988, 1225)],
    ['D', (815, 506), (991, 692)],
    ['D', (982, 510), (986, 871)],
    ['END'],
    ['D', (280, 1097), (453, 1223)],
    ['D', (986, 1056), (994, 1224)],
    ['END'],
    ['D', (990, 1049), (990, 1218)],
    ['END'],
    ['STAGE'],
]
chap06 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage06.ui
    ['D', (991, 1229), (798, 1221)],
    ['D', (986, 1413), (990, 1224)],
    ['D', (809, 1586), (991, 1398)],
    ['D', (804, 1407), (812, 1589)],
    ['END'],
    ['D', (812, 1589), (804, 1407)],
    ['END'],
    ['D', (804, 1407), (626, 1587)],
    ['D', (990, 1224), (990, 1054)],
    ['END'],
    ['STAGE'],
]
chap07 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage07.ui
    ['PREPARE'],
    ['D', (455, 1406), (626, 1415)],
    ['D', (636, 1584), (451, 1582)],
    ['PREPARE'],
    ['D', (626, 1415), (627, 864)],
    ['D', (452, 1410), (629, 868)],
    ['D', (633, 1584), (631, 1419)],
    ['D', (451, 1582), (452, 1231)],
    ['END'],
    ['D', (458, 1046), (95, 1048)],
    ['D', (631, 1419), (632, 1221)],
    ['D', (632, 1044), (637, 684)],
    ['END'],
    ['STAGE'],
]
chap08 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage08.ui
    ['D', (452, 1586), (267, 1397)],
    ['D', (623, 1588), (447, 1587)],
    ['D', (802, 1590), (631, 1590)],
    ['END'],
    ['D', (270, 1587), (88, 1221)],
    ['D', (447, 1587), (466, 1768)],
    ['D', (631, 1590), (267, 1586)],
    ['END'],
    ['D', (97, 1393), (86, 1579)],
    ['D', (466, 1768), (454, 1592)],
    ['D', (267, 1586), (89, 1397)],
    ['D', (267, 1397), (277, 1589)],
    ['END'],
    ['D', (454, 1592), (801, 1592)],
    ['D', (277, 1589), (99, 870)],
    ['D', (89, 1397), (97, 868)],
    ['END'],
    ['T', (633, 1594), (806, 1590), (805, 1412)],
    ['END'],
    ['D', (817, 1590), (813, 1228)],
    ['END'],
    ['STAGE'],
]
chap09 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage09.ui
    ['D', (271, 1412), (275, 1227)],
    ['T', (451, 1408), (808, 1416), (804, 1047)],
    ['D', (449, 1591), (448, 1414)],
    ['D', (453, 1760), (455, 1582)],
    ['END'],
    ['D', (275, 1227), (445, 1212)],
    ['D', (808, 1416), (444, 1025)],
    ['D', (455, 1582), (270, 1227)],
    ['END'],
    ['D', (445, 1212), (808, 1040)],
    ['END'],
    ['STAGE'],
]
chap10 = [
    ## /Users/gaoyunyun/Projs/FeScripts/FeLaya/laya/pages/group_03/FeStage10.ui
    ['PREPARE'],
    ['D', (268, 1584), (818, 1592)],
    ['D', (630, 1592), (453, 1588)],
    ['PREPARE'],
    ['D', (818, 1592), (810, 1409)],
    ['D', (627, 1588), (627, 1412)],
    ['D', (453, 1588), (453, 1404)],
    ['D', (267, 1590), (275, 1401)],
    ['END'],
    ['D', (810, 1409), (814, 1217)],
    ['D', (627, 1412), (455, 1224)],
    ['D', (275, 1401), (443, 1405)],
    ['D', (453, 1404), (454, 1217)],
    ['END'],
    ['D', (624, 1409), (628, 1592)],
    ['D', (454, 1217), (634, 1225)],
    ['D', (810, 1408), (630, 1409)],
    ['END'],
    ['D', (634, 1225), (634, 1029)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap01 + chap02 + chap03 + chap04 + chap05 + chap06 + chap07 + chap08 + chap09 + chap10
allstep = chap05+ chap06 + chap07 + chap08 + chap09 + chap10
# allstep = chap10

allstep += end
wd = WingDevice(device)
# wd.startFe(allstep)

allstep = chap01 + chap02 + chap03 + chap04 + chap05 + chap06 + chap07 + chap08 + chap09 + chap10 + end
# wd.loopFe(allstep, stam=False)
wd.loopFe(allstep, num=7)
