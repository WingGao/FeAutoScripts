# coding=utf-8
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys


def argbSame(argb, argb2, rate=5):
    r = argb2[1]
    g = argb2[2]
    b = argb2[3]
    return (r - rate <= argb[1] <= r + rate) and (g - rate <= argb[2] <= g + rate) and (b - rate <= argb[3] <= b + rate)


class FeState(object):
    MY_TURN = 1
    ENEMY_TURN = 2
    CHAIN_10 = 3  # 10连界面
    UNKNOWN = 100


class WingDevice(object):
    def __init__(self, device):
        self.device = device

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

    # 提醒用户，用闹钟
    def notifyUser(self):
        device = self.device
        return
        device.startActivity('com.android.deskclock/com.android.deskclock.AlarmsMainActivity')
        # TODO 更好的设置闹钟
        device.touch(917, 151, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.drag((696, 669), (704, 455), 1)
        MonkeyRunner.sleep(1)
        device.touch(540, 1945, MonkeyDevice.DOWN_AND_UP)
        # device.startActivity('com.android.deskclock.HandleSetAlarm','SET_TIMER','LENGTH=1')

    def startFe(self, allstep, can_exit=True):
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
                    if self.feState() == FeState.MY_TURN:
                        print 'action END match'
                        break
                    else:
                        print 'action END unmatch'
                        MonkeyRunner.sleep(1)
            elif cmd == 'STAGE':
                print 'wait STAGE'
                waitQ = range(60)
                for i in waitQ:  # 最多2分钟
                    device.touch(285, 1430, MonkeyDevice.DOWN_AND_UP)  # task
                    # 第一次忽律
                    if i == 0:
                        MonkeyRunner.sleep(5)
                        continue
                    elif i == len(waitQ) - 1:
                        sys.exit(1)  # 超时
                    if self.feState() == FeState.MY_TURN:
                        break
                    else:
                        MonkeyRunner.sleep(2)

            elif cmd == 'PREPARE':
                device.touch(726, 1955, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(5)
            elif cmd == 'EXIT':
                if can_exit:
                    self.notifyUser()
                    sys.exit(1)
                return
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
        print '[loopFe] start'
        cnt = 0
        print ''
        while True:
            cnt += 1
            print '[loopFe] round', cnt
            self.wait_state(FeState.CHAIN_10)
            # 点击开始
            self.device.touch(306, 722, MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            self.device.touch(290, 1275, MonkeyDevice.DOWN_AND_UP)  # 点击 开始战斗
            MonkeyRunner.sleep(1)
            # 体力不够
            for i in range(3):
                self.device.touch(313, 1191, MonkeyDevice.DOWN_AND_UP)  # 点击 回复/确定
                MonkeyRunner.sleep(1)

            self.wait_state(FeState.MY_TURN)
            self.startFe(allstep, False)

    def wait_state(self, state):
        while self.feState() != state:
            MonkeyRunner.sleep(1)

    def feState(self, mImg=None):
        '''判定当前画面状态
        :param mImg: MonkeyImage
        :return: FeState
        '''
        if mImg is None:
            mImg = self.device.takeSnapshot()
        wxfw = mImg.getRawPixel(280, 1985)  # 通过 危险范围 来判定
        if argbSame(wxfw, (-1, 169, 61, 85)):  # 正常,我的回合 (-1, 169, 61, 85)
            return FeState.MY_TURN
        elif argbSame(wxfw, (-1, 85, 31, 43)):
            # 敌人 (-1, 85, 31, 43)
            # 弹窗 (-1, 84, 30, 42)
            return FeState.ENEMY_TURN
        elif argbSame(mImg.getRawPixel(648, 837), (-1, 202, 39, 69)):  # 10连界面
            return FeState.CHAIN_10

        return FeState.UNKNOWN

    def test(self):
        for i in range(100):
            mImg = self.device.takeSnapshot()
            print mImg.getRawPixel(648, 837)
            MonkeyRunner.sleep(0.3)