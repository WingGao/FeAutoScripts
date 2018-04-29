# coding=utf-8
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys


def hello():
    print 'hello utils'


class WingDevice(object):
    def __init__(self, device):
        self.device = device
        self.normalFanweiBtn = self.getFanweiBtn()

    # def move(self, points, duration=1.0):
    #     '''
    #     移动
    #     :param points: [(x,y)...] 点1到点N
    #     :param duration: 总耗时
    #     :param step: 步骤
    #     :return:
    #     '''
    #     dx = (p2[0] - p1[0]) / step
    #     dy = (p2[1] - p1[1]) / step
    #     for i in range(0, step + 1):
    #         self.device.touch(p1[0] + dx * i, p1[1] + dy * i, MonkeyDevice.MOVE)
    #         MonkeyRunner.sleep(0.1)

    def move(self, p1, p2, duration=1.0, step=10):
        dx = (p2[0] - p1[0]) / step
        dy = (p2[1] - p1[1]) / step
        for i in range(0, step + 1):
            self.device.touch(p1[0] + dx * i, p1[1] + dy * i, MonkeyDevice.MOVE)
            MonkeyRunner.sleep(duration / step)

    def getFanweiBtn(self):
        img = self.device.takeSnapshot()
        btn = img.getSubImage((248, 1924, 140, 60))
        return btn

    # 提醒用户，用闹钟
    def notifyUser(self):
        device = self.device
        # return
        device.startActivity('com.android.deskclock/com.android.deskclock.AlarmsMainActivity')
        # TODO 更好的设置闹钟
        device.touch(917, 151, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.drag((696, 669), (704, 455), 1)
        MonkeyRunner.sleep(1)
        device.touch(540, 1945, MonkeyDevice.DOWN_AND_UP)
        # device.startActivity('com.android.deskclock.HandleSetAlarm','SET_TIMER','LENGTH=1')

    def startFe(self, allstep):
        device = self.device

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
                        self.move(points[i - 1], p, 0.5)
                        device.touch(p[0], p[1], MonkeyDevice.UP)
                    else:
                        self.move(points[i - 1], p, 0.5)
            elif cmd == 'END':
                device.touch(515, 1945, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                device.touch(299, 1062, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                for i in range(5):
                    device.touch(1027, 2088, MonkeyDevice.DOWN_AND_UP)  # 有时候已经stage了
                    btn = self.getFanweiBtn()
                    if self.normalFanweiBtn.sameAs(btn, 0.9):
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
                    btn = self.getFanweiBtn()
                    if self.normalFanweiBtn.sameAs(btn, 0.9):
                        print 'normalFanweiBtn STAGE match'
                        break
                    else:
                        print 'normalFanweiBtn STAGE unmatch'
                        MonkeyRunner.sleep(2)
            elif cmd == 'PREPARE':
                device.touch(726, 1955, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(5)
            elif cmd == 'EXIT':
                self.notifyUser()
                sys.exit(1)
            MonkeyRunner.sleep(1)

    def getStartBtn(self):
        '''
        获取章节页的标题栏，那个不会变
        :return:
        '''
        img = self.device.takeSnapshot()
        btn = img.getSubImage((235, 475, 79, 60))
        return btn

    def loopFe(self, allstep):
        '''
        全自动，包括开始，吃体力药，需要在章节列表页启动
        :param allstep:
        :return:
        '''
        normalBtn = self.getStartBtn()  # 正常状态的按钮
        # 点击开始
        self.device.touch(306, 722, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        watingBtn = self.getStartBtn()  # 等待状态的按钮
        self.device.touch(290, 1275, MonkeyDevice.DOWN_AND_UP)  # 点击 开始战斗
        # TODO 体力不够
        pass
