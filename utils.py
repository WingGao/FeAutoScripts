# coding=utf-8
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
import random
import datetime


def argbSame(argb, argb2, rate=5):
    r = argb2[1]
    g = argb2[2]
    b = argb2[3]
    return (r - rate <= argb[1] <= r + rate) and (g - rate <= argb[2] <= g + rate) and (b - rate <= argb[3] <= b + rate)


class FeState(object):
    MY_TURN = 1
    ENEMY_TURN = 2
    CHAIN_10 = 3  # 10连界面
    CHAPTER = 4  # 章节页面
    UNKNOWN = 100


class FeLevel(object):
    NORMAL = 0
    HARD = 1
    LUNATIC = 2
    INFERNAL = 3


class WingDevice(object):
    def __init__(self, device, debug=False):
        self.device = device
        self.width = int(self.device.getProperty('display.width'))
        self.height = int(self.device.getProperty('display.height'))
        self.dx = 0
        self.dy = 0  # 偏移修正
        self._debug = debug

        if self.width == 1080 and self.height >= 1920:
            if self.height != 2040:  # 2040是全面屏的尺寸，特别奇怪，不是2160
                self.dy = (self.height - 2160) / 2  # 因为是拿mate写的脚本
            else:
                self.dy += 72 / 2  # 导航栏
        else:
            raise Exception('not support w=%i h=%i' %
                            (self.width, self.height))
        self.debug('dy=%d' % self.dy)

    def debug(self, *args):
        if self._debug:
            print args
        return True

    def get_fix_point(self, point):
        np = (point[0], point[1] + self.dy)
        return np

    def move(self, p1, p2, duration=1.0, step=10):
        dx = (p2[0] - p1[0]) / step
        dy = (p2[1] - p1[1]) / step
        for i in range(0, step + 1):
            self.device.touch(p1[0] + dx * i, p1[1] +
                              dy * i, MonkeyDevice.MOVE)
            MonkeyRunner.sleep(duration / step)

    # 提醒用户，用闹钟
    def notifyUser(self):
        device = self.device
        return
        device.startActivity(
            'com.android.deskclock/com.android.deskclock.AlarmsMainActivity')
        # TODO 更好的设置闹钟
        device.touch(917, 151, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.drag((696, 669), (704, 455), 1)
        MonkeyRunner.sleep(1)
        device.touch(540, 1945, MonkeyDevice.DOWN_AND_UP)
        # device.startActivity('com.android.deskclock.HandleSetAlarm','SET_TIMER','LENGTH=1')

    def startFe(self, allstep, can_exit=True):
        device = self.device

        for stepIdx, step in enumerate(allstep):
            print '[%s][%i/%i] %r' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                      stepIdx + 1, len(allstep), step)
            cmd = step[0]
            if cmd == 'D':
                du = random.uniform(0.6, 1)

                device.drag(self.get_fix_point(
                    step[1]), self.get_fix_point(step[2]), du)
                if len(step) == 4:
                    MonkeyRunner.sleep(step[3])
            elif cmd == 'T':
                points = step[1:]
                du = random.uniform(0.2, 0.3)
                for i, p in enumerate(points):
                    if i == 0:
                        device.touch(p[0], p[1] + self.dy, MonkeyDevice.DOWN)
                    elif i == len(points) - 1:
                        self.move(self.get_fix_point(
                            points[i - 1]), self.get_fix_point(p), du)
                        device.touch(p[0], p[1] + self.dy, MonkeyDevice.UP)
                    else:
                        self.move(self.get_fix_point(
                            points[i - 1]), self.get_fix_point(p), du)
            elif cmd == 'END':
                device.touch(515, 1945 + self.dy, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                device.touch(299, 1062 + self.dy, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                while True:
                    device.touch(1045, 1870 + self.dy,
                                 MonkeyDevice.DOWN_AND_UP)  # 有时候已经stage了
                    if self.feState(check_btn=True) in [FeState.MY_TURN, FeState.CHAIN_10, FeState.CHAPTER]:
                        print 'action END match'
                        break
                    else:
                        print 'action END unmatch'
                        MonkeyRunner.sleep(1)
            elif cmd == 'STAGE':
                print 'wait STAGE'
                waitQ = range(60)
                for i in waitQ:  # 最多2分钟
                    device.touch(285, 1430 + self.dy,
                                 MonkeyDevice.DOWN_AND_UP)  # task
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
            elif cmd == 'AUTO':
                print 'click auto'
                # 自动战斗
                self.device.touch(120, 1975 + self.dy, MonkeyDevice.DOWN_AND_UP)  # 点击 设置
                MonkeyRunner.sleep(0.5)
                self.device.touch(300, 1250 + self.dy, MonkeyDevice.DOWN_AND_UP)  # 点击 自动
                MonkeyRunner.sleep(0.5)
                self.device.touch(300, 1100 + self.dy, MonkeyDevice.DOWN_AND_UP)  # 点击 确定
                MonkeyRunner.sleep(5)

            elif cmd == 'PREPARE':
                device.touch(726, 1955 + self.dy, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(5)
            elif cmd == 'EXIT':
                if can_exit:
                    self.notifyUser()
                    sys.exit(1)
                return
            MonkeyRunner.sleep(1)

    def loopFe(self, allstep, num=None, stam=True):
        '''
        全自动，包括开始，吃体力药，需要在章节列表页启动
        :param allstep:
        :param num: 最大次数
        :param stam: 自动吃药
        :return:
        '''
        print '[loopFe] start'
        cnt = 0
        print ''
        while True:
            if num is not None and cnt >= num:  # 最大次数
                return
            cnt += 1
            print '[loopFe] round', cnt
            self.wait_state(FeState.CHAIN_10)
            # 点击开始
            self.device.touch(306, 722 + self.dy, MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            self.device.touch(290, 1275 + self.dy,
                              MonkeyDevice.DOWN_AND_UP)  # 点击 开始战斗
            MonkeyRunner.sleep(1)
            # 体力不够
            for i in range(3):
                if not stam:  # 不自动吃药
                    break
                self.device.touch(313, 1191 + self.dy,
                                  MonkeyDevice.DOWN_AND_UP)  # 点击 回复/确定
                MonkeyRunner.sleep(1)

            self.wait_state(FeState.MY_TURN)
            self.startFe(allstep, False)

    def loop_dyz(self, num=None, level=FeLevel.INFERNAL):
        '''
                全自动大压制战，需要在章节列表页启动
                :param num: 最大次数
                :param level: 难度
                :return:
                '''
        print '[loop_dyz] start'
        cnt = 0
        print ''
        while True:
            if num is not None and cnt >= num:  # 最大次数
                return
            cnt += 1
            print '[loop_dyz] round', cnt
            self.wait_state(FeState.CHAPTER, check_btn=True)
            if level == FeLevel.LUNATIC:
                self.device.touch(310, 1070 + self.dy, MonkeyDevice.DOWN_AND_UP)
            elif level == FeLevel.INFERNAL:
                self.device.touch(310, 735 + self.dy, MonkeyDevice.DOWN_AND_UP)
            else:
                raise Exception('not support such level')
            MonkeyRunner.sleep(1)
            self.device.touch(310, 1630 + self.dy, MonkeyDevice.DOWN_AND_UP)  # 点击 开始战斗
            MonkeyRunner.sleep(1)

            self.wait_state(FeState.MY_TURN, duration=random.uniform(1, 5))
            self.startFe([['AUTO'], ['END']], False)
            # 结算
            self.wait_state(FeState.CHAPTER, check_btn=True)
            self.device.touch(310, 1825 + self.dy, MonkeyDevice.DOWN_AND_UP)  # 点击 确定
            MonkeyRunner.sleep(1)

    def loop_ghb(self, allstep, num=None, level=FeLevel.LUNATIC):
        '''
        全自动大英雄，需要在章节列表页启动
        :param allstep:
        :param num: 最大次数
        :param stam: 自动吃药
        :param level: 难度
        :return:
        '''
        print '[loop_ghb] start'
        cnt = 0
        print ''
        while True:
            if num is not None and cnt >= num:  # 最大次数
                return
            cnt += 1
            print '[loop_ghb] round', cnt
            self.wait_state(FeState.CHAPTER, check_btn=True)
            # 点击30
            if level == FeLevel.HARD:
                self.device.touch(310, 1412 + self.dy,
                                  MonkeyDevice.DOWN_AND_UP)
            elif level == FeLevel.LUNATIC:
                self.device.touch(310, 1070 + self.dy,
                                  MonkeyDevice.DOWN_AND_UP)
            else:
                raise Exception('not support such level')
            MonkeyRunner.sleep(1)
            self.device.touch(310, 1363 + self.dy,
                              MonkeyDevice.DOWN_AND_UP)  # 点击 开始战斗
            MonkeyRunner.sleep(1)

            self.wait_state(FeState.MY_TURN, duration=random.uniform(1, 5))
            self.startFe(allstep, False)

    def wait_state(self, state_or_list, duration=0, check_btn=False):
        while True:
            cs = self.feState(check_btn=check_btn)
            if isinstance(state_or_list, list) and cs in state_or_list:
                break
            elif cs == state_or_list:
                break
            MonkeyRunner.sleep(1)
        if duration > 0:
            MonkeyRunner.sleep(duration)

    def feState(self, mImg=None, check_btn=False):
        '''判定当前画面状态
        :param mImg: MonkeyImage
        :param check_btn: 检查是否有按钮
        :return: FeState
        '''
        if mImg is None:
            mImg = self.device.takeSnapshot()
        try:
            wxfw = mImg.getRawPixel(280, 1985 + self.dy)  # 通过 危险范围 来判定
            self.debug('[feState] MY_TURN val %r' % (wxfw,))
            if argbSame(wxfw, (-1, 169, 61, 85)):  # 正常,我的回合 (-1, 169, 61, 85)
                self.debug('[feState] MY_TURN ok')
                return FeState.MY_TURN
            elif argbSame(wxfw, (-1, 85, 31, 43)):
                # 敌人 (-1, 85, 31, 43)
                # 弹窗 (-1, 84, 30, 42)
                return FeState.ENEMY_TURN
            elif argbSame(mImg.getRawPixel(648, 837 + self.dy), (-1, 202, 39, 69)):  # 10连界面
                return FeState.CHAIN_10
            elif argbSame(mImg.getRawPixel(143, 350 + self.dy), (-1, 0, 132, 193)):  # 章节页面，通过队伍编号
                return FeState.CHAPTER
            elif argbSame(mImg.getRawPixel(800, 183 + self.dy), (-1, 71, 33, 39)):  # 跳过按钮
                print 'FEH get skip'
                self.device.touch(800, 183 + self.dy, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            elif argbSame(mImg.getRawPixel(267, 1123 + self.dy), (-1, 55, 83, 72)):  # 错误803-3101
                # TODO 添加断线重连
                print 'FEH get an error'
                self.device.touch(267, 1123 + self.dy,
                                  MonkeyDevice.DOWN_AND_UP)
            elif argbSame(mImg.getRawPixel(313, 1191 + self.dy), (-1, 63, 89, 74)):  # 回复体力成功，关闭
                print 'stamina full success'
                self.device.touch(313, 1191 + self.dy,
                                  MonkeyDevice.DOWN_AND_UP)
            elif check_btn:
                self.fe_state_has_btn(mImg)
        except Exception, e:
            print 'error on feState', e

        return FeState.UNKNOWN

    def fe_state_has_btn(self, img=None, touch=True):
        if img is None:
            img = self.device.takeSnapshot()
            # step = 3
        btn_colors = [
            (-1, 77, 124, 98),
            (-1, 77, 117, 94),
            (-1, 75, 110, 89),
            (-1, 74, 106, 86),
            (-1, 72, 101, 83),
            (-1, 71, 97, 80),
            (-1, 69, 94, 77),
            (-1, 68, 91, 75),
            (-1, 67, 89, 72),
            (-1, 64, 88, 71),
            (-1, 62, 87, 71),
            (-1, 60, 88, 70),
            (-1, 59, 89, 70),
            (-1, 55, 91, 69),
            (-1, 52, 94, 69),
            (-1, 49, 97, 69),
            (-1, 48, 103, 70),
            (-1, 47, 107, 71),
            (-1, 46, 112, 73),
            (-1, 49, 120, 77),
            (-1, 52, 127, 82),
            (-1, 61, 139, 91),
            (-1, 71, 152, 102),
            (-1, 85, 165, 116),
            (-1, 99, 178, 130),
        ]
        # 1380 - 1900
        for i in range(1380, 1900, 1):
            py = i + self.dy
            has_btn = 0

            # self.debug('[fe_state_has_btn] y=%i color=%r' % (i, img.getRawPixel(320, i + self.dy)))
            for j, p in enumerate(btn_colors):
                if argbSame(img.getRawPixel(320, py + j * 3), p):
                    has_btn += 1
            self.debug('[fe_state_has_btn] y=%i has_btn=%i' % (i, has_btn))
            # 说明有一个关闭按钮
            if has_btn >= len(btn_colors) * 0.75:
                print 'find ok btn', 320, py
                if touch:
                    self.device.touch(320, py, MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                return

    def get_ok_btn(self):
        img = self.device.takeSnapshot()
        x = 320
        for i in range(1625, 1700, 3):
            print img.getRawPixel(x, i)

        # for i in range(250, 320, 1):
        #     print img.getRawPixel(x, 1625)

    def test(self):
        print self.device.getProperty('display.width')
        print self.device.getProperty('display.height')
        print self.device.getProperty('display.density')
        print 'feState', self.feState(check_btn=False)
        self.fe_state_has_btn()
        mImg = self.device.takeSnapshot()
        print 'feState chapter', mImg.getRawPixel(143, 350 + self.dy)  # (-1, 0, 132, 193)):  # 章节页面，通过队伍编号
        # print mImg.getRawPixel(143, 350 + self.dy)
        step = 50
        for i in range(step):
            y = 1985 + i - step / 2
            # for j in range(step):
            #     x = 143 + j - step / 2
            x = 280
            px = mImg.getRawPixel(x, y + self.dy)
            print x, y, px
            if argbSame(px, (-1, 169, 61, 85)):
                print '==>', x, y
        # print mImg.getRawPixel(320, 1430 + i)
