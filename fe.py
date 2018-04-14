# coding=utf-8
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
import time

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()


# 10连
# 罗伊-近防3 迪幽特-生命2 温蒂-防大1 希玛-防守指挥1
#

def move(p1, p2, duration=1.0, step=10):
    dx = (p2[0] - p1[0]) / step
    dy = (p2[1] - p1[1]) / step
    for i in range(0, step + 1):
        device.touch(p1[0] + dx * i, p1[1] + dy * i, MonkeyDevice.MOVE)
        MonkeyRunner.sleep(0.1)


def getFanweiBtn():
    img = device.takeSnapshot()
    btn = img.getSubImage((248, 1924, 140, 60))
    return btn


# 提醒用户，用闹钟
def notifyUser():
    return 
    device.startActivity('com.android.deskclock/com.android.deskclock.AlarmsMainActivity')
    # TODO 更好的设置闹钟
    device.touch(917, 151, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    device.drag((696, 669), (704, 455), 1)
    MonkeyRunner.sleep(1)
    device.touch(540, 1945, MonkeyDevice.DOWN_AND_UP)
    # device.startActivity('com.android.deskclock.HandleSetAlarm','SET_TIMER','LENGTH=1')


# notifyUser()
# sys.exit(2)

print 'Chap1-2 10连'
scriptStarttime = time.time()
# chap 1

chap01 = [
    ['D', (267, 1055), (810, 1051)],
    ['D', (269, 1235), (99, 1226)],
    ['D', (91, 1053), (270, 1057)],
    ['END'],
    ['D', (281, 1058), (809, 1059)],
    ['T', (455, 1046), (456, 1238), (810, 1232)],
    ['STAGE'],  # next stage
]
chap02 = [
    ['T', (806, 1049), (790, 710), (633, 700)],
    ['D', (803, 1417), (800, 1590)],
    ['D', (979, 1236), (999, 1407)],
    ['END'],
    ['D', (811, 1595), (624, 1592)],
    ['END'],
    ['D', (811, 1595), (624, 1592)],
    ['D', (974, 1408), (644, 1611)],
    ['STAGE'],
]
chap03t04 = [
    ## chap3
    ['PREPARE'],
    ['D', (444, 1598), (633, 1582)],
    ['PREPARE'],
    ['D', (633, 1581), (608, 1232)],
    ['D', (451, 1591), (447, 1232)],
    ['END'],
    ['D', (621, 1230), (611, 855)],
    ['D', (438, 1223), (450, 690)],
    ['END'],
    ['STAGE'],
    ## chap4
    ['D', (447, 1776), (439, 1589)],
    ['D', (631, 1589), (447, 1766)],
    ['D', (981, 1592), (636, 1588)],
    ['D', (800, 1767), (794, 1590)],
    ['END'],
    ['D', (443, 1598), (254, 1591)],
    ['D', (631, 1596), (444, 1588)],
    ['D', (780, 1585), (621, 1580)],
    ['END'],
    ['D', (250, 1582), (62, 1571)],
    ['D', (441, 1602), (264, 1240)],
    ['END'],
    ['D', (629, 1590), (612, 1399)],
    ['D', (258, 1580), (457, 1576)],
    ['END'],
    ['D', (628, 1583), (618, 1403)],
    ['D', (447, 1577), (624, 1579)],
    ['END'],
    ['STAGE'],

]
chap05 = [
    ## chap5
    ['D', (801, 506), (623, 698)],
    ['END'],
    ['D', (615, 693), (275, 686)],
    ['END'],
    ['T', (274, 697), (81, 861), (278, 882)],
    ['D', (982, 872), (987, 701)],
    ['END'],
    ['D', (77, 879), (77, 1256)],
    ['D', (991, 875), (978, 1043)],
    ['END'],
    ['D', (991, 875), (978, 1043)],
    ['D', (977, 692), (974, 512)],
    ['D', (791, 698), (985, 1058)],
    ['STAGE'],
]

chap06 = [
    ## chap6
    ['D', (984, 1221), (793, 1209)],
    ['D', (995, 1416), (984, 1223)],
    ['D', (802, 1596), (1001, 1590)],
    ['D', (796, 1412), (788, 1602)],
    ['END'],
    ['D', (988, 1614), (992, 1406)],
    ['D', (799, 1583), (806, 1420)],
    ['END'],
    ['D', (978, 1232), (979, 1040)],
    ['END'],
    ['STAGE'],
]
otherChap = [
    ## chap7
    ['PREPARE'],
    ['D', (445, 1414), (625, 1412)],
    ['PREPARE'],
    ['D', (626, 1409), (632, 866)],
    ['T', (447, 1416), (420, 1055), (627, 880)],
    ['END'],
    ['D', (453, 1046), (83, 1050)],
    ['D', (621, 1034), (623, 700)],
    ['STAGE'],
    ## chap8
    ['D', (449, 1587), (251, 1378)],
    ['D', (626, 1595), (445, 1592)],
    ['D', (805, 1592), (632, 1596)],
    ['END'],
    ['D', (434, 1598), (446, 1772)],
    ['D', (627, 1598), (448, 1586)],
    ['END'],
    ['D', (266, 1592), (94, 1585)],
    ['D', (252, 1382), (260, 1578)],
    ['D', (465, 1772), (268, 1778)],
    ['D', (443, 1587), (277, 1762)],
    ['END'],
    ['D', (273, 1581), (627, 1598)],
    ['D', (469, 1763), (661, 1778)],
    ['END'],
    ['T', (618, 1787), (622, 1595), (797, 1585)],
    ['D', (245, 1588), (638, 1589)],
    ['STAGE'],

]
chap09 = [
    ['D', (263, 1412), (265, 1036)],
    ['T', (452, 1409), (803, 1418), (814, 1058)],
    ['D', (451, 1774), (442, 1600)],
    ['END'],
    ['D', (267, 1040), (258, 1413)],
    ['D', (797, 1412), (616, 1418)],
    ['D', (439, 1590), (443, 1396)],
    ['END'],
    ['END'],
    ['STAGE'],
]
chap10 = [
    ['PREPARE'],
    ['D', (809, 1598), (255, 1586)],
    ['D', (618, 1584), (449, 1587)],
    ['PREPARE'],
    ['D', (265, 1595), (259, 1416)],
    ['D', (443, 1585), (449, 1407)],
    ['D', (632, 1590), (616, 1401)],
    ['D', (810, 1592), (767, 1411)],
    ['END'],
    ['D', (266, 1390), (265, 1215)],
    ['T', (615, 1399), (622, 1043), (442, 1232)],
    ['D', (789, 1383), (792, 1038)],
    ['END'],
    ['EXIT'],
]
allstep = chap01 + chap02 + chap03t04 + chap05 + chap06 + otherChap + chap09 + chap10
# allstep =  chap02 + chap03t04+ chap05 + chap06 + otherChap + chap09 + chap10
# allstep = chap05 + chap06 + otherChap + chap09 + chap10

# 原始'威胁范围'按钮
normalFanweiBtn = getFanweiBtn()

for step in allstep:
    cmd = step[0]
    if cmd == 'D':
        du = 0.5
        if len(step) == 4:
            du = step[3]
        device.drag(step[1], step[2], du)
    elif cmd == 'T':
        points = step[1:]
        for i, p in enumerate(points):
            if i == 0:
                device.touch(p[0], p[1], MonkeyDevice.DOWN)
            elif i == len(points) - 1:
                move(points[i - 1], p)
                device.touch(p[0], p[1], MonkeyDevice.UP)
            else:
                move(points[i - 1], p)
    elif cmd == 'END':
        device.touch(515, 1945, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.touch(299, 1062, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        for i in range(5):
            device.touch(1027, 2088, MonkeyDevice.DOWN_AND_UP)  # 有时候已经stage了
            btn = getFanweiBtn()
            if normalFanweiBtn.sameAs(btn, 0.9):
                print 'normalFanweiBtn END match'
                break
            else:
                print 'normalFanweiBtn END unmatch'
                MonkeyRunner.sleep(1)
    elif cmd == 'STAGE':
        waitQ = range(60)
        for i in waitQ:  # 最多2分钟
            device.touch(285, 1430, MonkeyDevice.DOWN_AND_UP)  # task
            # 第一次忽律
            if i == 0:
                MonkeyRunner.sleep(5)
                continue
            elif i == len(waitQ) - 1:
                sys.exit(1)  # 超时
            btn = getFanweiBtn()
            if normalFanweiBtn.sameAs(btn, 0.9):
                print 'normalFanweiBtn STAGE match'
                break
            else:
                print 'normalFanweiBtn STAGE unmatch'
                MonkeyRunner.sleep(2)
    elif cmd == 'PREPARE':
        device.touch(726, 1955, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(5)
    elif cmd == 'EXIT':
        scriptDuration = time.time() - scriptStarttime
        print 'script complete use %i seconds' % scriptDuration
        notifyUser()
        sys.exit(1)
    MonkeyRunner.sleep(1)
