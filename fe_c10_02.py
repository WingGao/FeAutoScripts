# coding=utf-8
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
import platform
if platform.system() == 'Windows':
    # print sys.path
    sys.path.append(sys.path[0].split(':', 1)[1])

from utils import WingDevice
import time

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# 10连
# 罗伊-近防3 迪幽特-生命2 温蒂-防大1 希玛-防守指挥1
#

print 'Chap1-2 10连'
scriptStarttime = time.time()
chap01 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage01.ui
    ['D', (92, 1234), (445, 1233)],
    ['D', (274, 1046), (811, 1037)],
    ['D', (92, 1050), (270, 1052)],
    ['END'],
    ['D', (451, 1054), (813, 1045)],
    ['D', (445, 1233), (639, 1400)],
    ['D', (269, 1230), (640, 1402)],
    ['END'],
    ['STAGE'],
]
chap02 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage02.ui
    ['D', (808, 1409), (804, 1593)],
    ['D', (812, 1046), (636, 688)],
    ['D', (996, 1231), (986, 1419)],
    ['END'],
    ['END'],
    ['D', (804, 1593), (642, 1603)],
    ['D', (986, 1419), (641, 1604)],
    ['END'],
    ['STAGE'],
]
chap03 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage03.ui
    ['PREPARE'],
    ['D', (450, 1593), (632, 1583)],
    ['PREPARE'],
    ['D', (632, 1583), (632, 1221)],
    ['D', (456, 1584), (456, 1223)],
    ['D', (452, 1769), (452, 1408)],
    ['D', (633, 1767), (633, 1409)],
    ['END'],
    ['D', (456, 1223), (448, 877)],
    ['D', (632, 1221), (632, 873)],
    ['D', (452, 1408), (448, 1059)],
    ['D', (633, 1409), (625, 1221)],
    ['END'],
    ['D', (448, 1059), (452, 692)],
    ['D', (628, 1037), (452, 687)],
    ['END'],
    ['STAGE'],
]
chap04 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage04.ui
    ['D', (451, 1773), (263, 1576)],
    ['D', (630, 1590), (458, 1762)],
    ['D', (989, 1582), (627, 1589)],
    ['D', (814, 1769), (804, 1585)],
    ['END'],
    ['D', (263, 1576), (91, 1585)],
    ['T', (627, 1589), (266, 1584), (264, 1232)],
    ['D', (804, 1585), (632, 1589)],
    ['END'],
    ['D', (91, 1585), (451, 1590)],
    ['END'],
    ['D', (632, 1589), (632, 1411)],
    ['D', (451, 1590), (630, 1594)],
    ['END'],
    ['STAGE'],
]
chap05 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage05.ui
    ['D', (807, 507), (617, 693)],
    ['END'],
    ['D', (617, 693), (275, 689)],
    ['END'],
    ['D', (811, 687), (815, 506)],
    ['D', (989, 690), (815, 690)],
    ['D', (985, 871), (997, 688)],
    ['END'],
    ['D', (815, 690), (455, 694)],
    ['D', (275, 689), (635, 697)],
    ['D', (997, 688), (989, 506)],
    ['END'],
    ['D', (989, 506), (989, 869)],
    ['END'],
    ['D', (997, 690), (985, 1047)],
    ['D', (815, 506), (984, 1051)],
    ['END'],
    ['STAGE'],
]
chap06 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage06.ui
    ['D', (991, 1229), (798, 1221)],
    ['D', (986, 1413), (990, 1224)],
    ['D', (809, 1586), (991, 1406)],
    ['D', (804, 1407), (812, 1589)],
    ['END'],
    ['D', (798, 1221), (623, 1213)],
    ['D', (812, 1589), (804, 1407)],
    ['END'],
    ['D', (804, 1407), (626, 1587)],
    ['D', (990, 1224), (990, 1054)],
    ['END'],
    ['STAGE'],
]
chap07 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage07.ui
    ['PREPARE'],
    ['D', (455, 1406), (632, 1406)],
    ['PREPARE'],
    ['D', (632, 1406), (627, 864)],
    ['D', (452, 1405), (629, 868)],
    ['D', (453, 1591), (452, 1222)],
    ['D', (636, 1584), (452, 1405)],
    ['END'],
    ['D', (632, 1044), (637, 684)],
    ['D', (458, 1046), (458, 680)],
    ['D', (452, 1222), (280, 1044)],
    ['D', (452, 1405), (437, 1228)],
    ['END'],
    ['STAGE'],
]
chap08 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage08.ui
    ['D', (452, 1586), (267, 1397)],
    ['D', (623, 1588), (451, 1588)],
    ['D', (802, 1590), (631, 1590)],
    ['END'],
    ['D', (451, 1588), (466, 1768)],
    ['D', (631, 1590), (461, 1585)],
    ['END'],
    ['D', (270, 1587), (86, 1582)],
    ['D', (267, 1397), (98, 1221)],
    ['D', (461, 1585), (281, 1773)],
    ['END'],
    ['T', (466, 1768), (462, 1595), (627, 1590)],
    ['D', (274, 1395), (630, 1586)],
    ['D', (281, 1773), (460, 1773)],
    ['END'],
    ['D', (460, 1773), (455, 1238)],
    ['END'],
]
chap09 = [
    ## D:\Projs\FeAutoScripts\\FeLaya\laya\pages\group_02\FeStage09.ui
    ['D', (271, 1412), (275, 1227)],
    ['T', (451, 1408), (808, 1416), (804, 1047)],
    ['D', (449, 1591), (629, 1417)],
    ['D', (453, 1760), (628, 1594)],
    ['END'],
    ['D', (808, 1416), (451, 1404)],
    ['D', (275, 1227), (275, 1030)],
    ['D', (628, 1594), (811, 1409)],
    ['D', (629, 1417), (815, 1409)],
    ['END'],
    ['D', (267, 1219), (275, 1050)],
    ['D', (451, 1404), (273, 1228)],
    ['END'],
    ['STAGE'],
]
chap10 = [
    ## D:\Projs\FeLaya\laya\pages\FeStage10.ui
    ['PREPARE'],
    ['D', (268, 1584), (818, 1592)],
    ['D', (630, 1592), (453, 1588)],
    ['PREPARE'],
    ['D', (818, 1592), (810, 1409)],
    ['D', (627, 1588), (627, 1404)],
    ['D', (453, 1588), (453, 1404)],
    ['D', (267, 1590), (275, 1401)],
    ['END'],
    ['D', (810, 1409), (814, 1217)],
    ['D', (627, 1404), (455, 1224)],
    ['D', (275, 1401), (271, 1229)],
    ['END'],
    ['D', (453, 1404), (634, 1225)],
    ['D', (271, 1409), (446, 1220)],
    ['END'],
    ['D', (634, 1225), (634, 1029)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap01 + chap02 + chap03 + chap04 + chap05 + chap06 + chap07 + chap08 + chap09 + chap10
allstep =chap06 + chap07 + chap08 + chap09 + chap10
# allstep = chap09 + chap10

allstep += end
wd = WingDevice(device)
wd.startFe(allstep)