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
# time 2018-05-03 01:37:53.628000
chap01 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage01.ui
    ['D', (274, 1046), (812, 1042)],
    ['D', (92, 1234), (450, 1232)],
    ['D', (92, 1050), (267, 1051)],
    ['END'],
    ['D', (451, 1047), (813, 1039)],
    ['D', (450, 1232), (636, 1406)],
    ['END'],
    ['STAGE'],
]
chap02 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage02.ui
    ['D', (808, 1409), (804, 1593)],
    ['T', (812, 1046), (811, 682), (632, 688)],
    ['D', (996, 1231), (986, 1419)],
    ['END'],
    ['D', (986, 1590), (986, 1762)],
    ['D', (804, 1593), (985, 1580)],
    ['END'],
    ['D', (985, 1580), (642, 1603)],
    ['D', (986, 1762), (637, 1607)],
    ['END'],
    ['STAGE'],
]
chap03 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage03.ui
    ['PREPARE'],
    ['D', (450, 1593), (632, 1583)],
    ['D', (633, 1767), (458, 1586)],
    ['PREPARE'],
    ['D', (632, 1583), (632, 1221)],
    ['D', (458, 1586), (448, 1231)],
    ['D', (634, 1766), (622, 1391)],
    ['D', (455, 1765), (446, 1392)],
    ['END'],
    ['D', (632, 1221), (632, 873)],
    ['D', (448, 1231), (448, 881)],
    ['END'],
    ['D', (448, 1044), (451, 690)],
    ['END'],
    ['STAGE'],
]
chap04 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage04.ui
    ['D', (451, 1773), (258, 1578)],
    ['D', (630, 1590), (458, 1762)],
    ['D', (989, 1582), (627, 1589)],
    ['D', (814, 1769), (804, 1585)],
    ['END'],
    ['D', (458, 1762), (269, 1771)],
    ['D', (258, 1578), (273, 1225)],
    ['T', (627, 1589), (265, 1590), (260, 1212)],
    ['D', (804, 1585), (632, 1589)],
    ['END'],
    ['D', (255, 1403), (621, 1216)],
    ['D', (632, 1589), (623, 1037)],
    ['END'],
    ['D', (623, 1037), (815, 1023)],
    ['END'],
    ['STAGE'],
]
chap05 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage05.ui
    ['D', (807, 507), (617, 693)],
    ['END'],
    ['D', (617, 693), (275, 689)],
    ['END'],
    ['D', (811, 687), (815, 506)],
    ['D', (985, 871), (982, 510)],
    ['D', (989, 690), (990, 873)],
    ['END'],
    ['D', (275, 689), (101, 1062)],
    ['D', (990, 873), (991, 693)],
    ['D', (815, 506), (811, 692)],
    ['END'],
    ['D', (91, 876), (99, 1229)],
    ['D', (811, 692), (456, 698)],
    ['D', (991, 693), (802, 510)],
    ['D', (982, 510), (636, 696)],
    ['END'],
    ['D', (99, 1229), (455, 1226)],
    ['D', (456, 698), (95, 692)],
    ['D', (802, 510), (453, 506)],
    ['D', (636, 696), (273, 690)],
    ['END'],
    ['D', (455, 1226), (636, 1043)],
    ['D', (453, 506), (92, 509)],
    ['D', (273, 690), (89, 874)],
    ['END'],
    ['D', (95, 692), (453, 700)],
    ['T', (92, 509), (269, 697), (452, 697)],
    ['D', (636, 1043), (640, 1399)],
    ['D', (89, 874), (455, 694)],
    ['END'],
    ['D', (640, 1399), (989, 1411)],
    ['END'],
    ['STAGE'],
]
chap06 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage06.ui
    ['PREPARE'],
    ['D', (809, 1586), (809, 1405)],
    ['PREPARE'],
    ['D', (991, 1229), (816, 1229)],
    ['D', (986, 1413), (998, 1229)],
    ['D', (809, 1405), (809, 1222)],
    ['END'],
    ['D', (809, 1412), (985, 1406)],
    ['D', (810, 1586), (816, 1415)],
    ['END'],
    ['D', (816, 1415), (620, 1602)],
    ['D', (998, 1229), (992, 1055)],
    ['END'],
    ['STAGE'],
]
chap07 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage07.ui
    ['PREPARE'],
    ['D', (455, 1406), (626, 1415)],
    ['D', (636, 1584), (451, 1582)],
    ['PREPARE'],
    ['D', (626, 1415), (627, 864)],
    ['D', (452, 1410), (629, 868)],
    ['D', (633, 1584), (627, 1231)],
    ['D', (451, 1582), (452, 1231)],
    ['END'],
    ['D', (452, 1231), (99, 1046)],
    ['D', (458, 1046), (637, 868)],
    ['D', (627, 1231), (446, 1225)],
    ['D', (632, 1044), (641, 873)],
    ['END'],
    ['D', (269, 1038), (639, 684)],
    ['END'],
    ['STAGE'],
]
chap08 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage08.ui
    ['D', (452, 1586), (267, 1397)],
    ['D', (623, 1588), (447, 1587)],
    ['D', (802, 1590), (631, 1590)],
    ['END'],
    ['D', (270, 1587), (286, 1764)],
    ['D', (267, 1397), (264, 1586)],
    ['D', (447, 1587), (271, 1398)],
    ['D', (631, 1590), (463, 1582)],
    ['END'],
    ['T', (271, 1398), (264, 1224), (100, 1213)],
    ['D', (463, 1582), (100, 1214)],
    ['END'],
    ['D', (278, 1213), (630, 1216)],
    ['D', (96, 1393), (454, 1587)],
    ['D', (286, 1764), (270, 1395)],
    ['D', (264, 1586), (95, 1590)],
    ['END'],
    ['D', (270, 1395), (274, 1226)],
    ['D', (95, 1590), (95, 1233)],
    ['D', (446, 1221), (632, 1412)],
    ['D', (454, 1587), (94, 1407)],
    ['END'],
    ['T', (632, 1412), (808, 1409), (811, 1586)],
    ['END'],
    ['T', (809, 1410), (810, 1593), (989, 1591)],
    ['END'],
    ['D', (819, 1579), (989, 1406)],
    ['END'],
    ['STAGE'],
]
chap09 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage09.ui
    ['D', (271, 1412), (275, 1227)],
    ['D', (449, 1591), (623, 1414)],
    ['T', (451, 1408), (808, 1416), (804, 1047)],
    ['D', (453, 1760), (452, 1407)],
    ['END'],
    ['D', (623, 1414), (274, 1229)],
    ['D', (267, 1412), (628, 1408)],
    ['END'],
    ['D', (452, 1407), (984, 1415)],
    ['D', (808, 1416), (813, 1042)],
    ['D', (628, 1408), (808, 1040)],
    ['D', (274, 1229), (274, 1041)],
    ['END'],
    ['STAGE'],
]
chap10 = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage10.ui
    ['PREPARE'],
    ['D', (268, 1584), (818, 1592)],
    ['D', (630, 1592), (453, 1588)],
    ['PREPARE'],
    ['D', (818, 1592), (810, 1409)],
    ['D', (627, 1588), (627, 1412)],
    ['D', (453, 1588), (453, 1404)],
    ['D', (268, 1590), (275, 1401)],
    ['END'],
    ['T', (453, 1404), (636, 1210), (448, 1220)],
    ['D', (275, 1401), (443, 1405)],
    ['D', (627, 1412), (455, 1224)],
    ['END'],
    ['END'],
    ['D', (634, 1225), (634, 1029)],
    ['END'],
    # ['STAGE'],
]

end = [
    ['EXIT']
]

allstep = chap01 + chap02 + chap03 + chap04 + chap05 + chap06 + chap07 + chap08 + chap09 + chap10
allstep = chap04 + chap05 + chap06 + chap07 + chap08 + chap09 + chap10
# allstep =  chap06 + chap07 + chap08 + chap09 + chap10
allstep = chap09 + chap10
# allstep = chap10

allstep += end
wd = WingDevice(device)
# wd.startFe(allstep)

allstep = chap01 + chap02 + chap03 + chap04 + chap05 + chap06 + chap07 + chap08 + chap09 + chap10 + end
# wd.loopFe(allstep, stam=False)
wd.loopFe(allstep)

# 大英雄 仓鸦
chap_cy = [
    ## D:\Projs\FeAutoScripts\FeLaya/laya/pages/group_04/FeStage_cy.ui
    ['D', (274, 864), (631, 1230)],
    ['D', (93, 867), (89, 1229)],
    ['D', (88, 686), (274, 868)],
    ['D', (92, 1047), (91, 687)],
    ['END'],
    ['D', (455, 1052), (94, 1044)],
    ['D', (91, 687), (87, 507)],
    ['D', (274, 868), (91, 868)],
    ['END'],
    ['D', (91, 868), (277, 864)],
    ['END'],
    ['D', (94, 1044), (90, 868)],
    ['END'],
    ['D', (277, 864), (277, 1051)],
    ['D', (87, 507), (95, 869)],
    ['END'],
    ['D', (95, 869), (273, 1048)],
    ['D', (94, 688), (98, 868)],
    ['D', (273, 874), (97, 686)],
    ['END'],
    ['D', (273, 1048), (460, 1048)],
    ['D', (89, 1229), (636, 1043)],
    ['END'],
    ['D', (451, 1043), (272, 1418)],
    ['D', (271, 1040), (632, 1052)],
    ['END'],
    ['D', (460, 1422), (275, 1580)],
    ['END'],
    # ['STAGE'],
]
chap_am = [
## /Users/suamo/Projs/FeAutoScripts/FeLaya/laya/pages/group_04/FeStage_am.ui
['D', (808, 511), (463, 517)],
['D', (444, 1765), (810, 1769)],
['D', (628, 1764), (993, 1768)],
['D', (979, 1048), (802, 1398)],
['END'],
['D', (463, 517), (98, 514)],
['D', (810, 1769), (994, 1582)],
['D', (802, 1398), (811, 1219)],
['D', (993, 1768), (812, 1764)],
['END'],
['D', (994, 1582), (990, 1221)],
['D', (806, 1405), (457, 1413)],
['END'],
['D', (623, 1410), (623, 1585)],
['END'],
# ['STAGE'],
]
# wd.loop_ghb(chap_cy + end)
# wd.loop_ghb(chap_am + end)
