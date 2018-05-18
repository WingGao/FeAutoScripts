# coding=utf-8
import json
import os
import datetime


class Action(object):
    def __init__(self):
        self.index = 0
        self.x = 0
        self.y = 0


class Character(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.actions = dict()  # key=index, v=Action
        self.lastAction = Action()
        self.currentActions = []  # 当前移动的轨迹

    def end_action(self):
        acts = []
        # acts.append(self.name)
        if len(self.currentActions) < 2:
            return None
        if len(self.currentActions) == 2:
            acts.append('D')
        else:
            acts.append('T')
        for a in self.currentActions:
            acts.append((a.x + 90, a.y + 90))
        self.currentActions = []
        return acts


def parse_file(f):
    print 'parse', f
    laya = None
    with open(f) as r:
        laya = json.load(r)
    character_dict = {}  # key=id, v=Character
    for cj in laya['child']:
        name = cj['props'].get('name')
        if cj['type'] == 'Sprite' and name is not None:
            ca = Character(name, cj['compId'])
            print 'get %s(id=%d)' % (ca.name, ca.id)
            character_dict[ca.id] = ca

    for anim in laya['animations']:
        if anim['name'] == 'ani1':
            for node in anim['nodes']:
                cha = character_dict[node['target']]
                xi = 0
                yi = 0
                keyframesX = node['keyframes']['x']
                keyframesY = node['keyframes'].get('y', [])
                keyXIndex = 0
                keyYIndex = 0
                while True:
                    px = None
                    py = None

                    if xi < len(keyframesX):
                        keyX = keyframesX[xi]
                        px = keyX['value']
                        keyXIndex = keyX['index']
                    else:
                        keyXIndex = None
                    xi += 1
                    if yi < len(keyframesY):
                        keyY = keyframesY[yi]
                        py = keyY['value']
                        keyYIndex = keyY['index']
                    else:
                        keyYIndex = None
                    yi += 1

                    if px is None and py is None:
                        break

                    if (keyXIndex is None or keyXIndex > keyYIndex) and keyYIndex is not None:  # 缺x
                        xi -= 1
                        px = cha.lastAction.x
                        keyXIndex = keyYIndex
                    elif (keyYIndex is None or keyXIndex < keyYIndex) and keyXIndex is not None:  # 缺y
                        yi -= 1
                        py = cha.lastAction.y
                        keyYIndex = keyXIndex

                    act = Action()
                    act.index = keyXIndex
                    act.x = px
                    act.y = py
                    cha.lastAction = act
                    cha.actions[act.index] = act
                print 'character %s ok' % cha.name

    # 时间线
    steps = []
    i = 0
    check_prepare = False
    names = ['p1', 'p2', 'p3', 'p4']
    chaIds = []
    chaEnd = None
    chaPre = None
    for cha in character_dict.values():
        if cha.name in names:
            chaIds.append(cha.id)
        elif cha.name == 'end':
            chaEnd = cha
        elif cha.name == 'prepare':
            chaPre = cha

    chaSeqs = []

    # 重置状态
    def setCharPos(actIndex):
        for id in chaIds:
            cha = character_dict.get(id)
            act = cha.actions.get(actIndex)
            if act is not None:
                cha.lastAction = act

    while i < 100:
        if i == 0:
            setCharPos(0)
            if chaPre is not None:
                if chaPre.actions.get(0) is not None:
                    # 准备阶段
                    check_prepare = True
                    steps.append(['PREPARE'])
            i += 1
        elif check_prepare:
            if chaPre.actions.get(i) is not None:
                check_prepare = False
                for cha in chaSeqs:
                    steps.append(cha.end_action())
                steps.append(['PREPARE'])
                chaSeqs = []
                i += 1
                setCharPos(i)
                i += 1

        if chaEnd.actions.get(i) is not None:
            # 结束
            for cha in chaSeqs:
                steps.append(cha.end_action())
            steps.append(['END'])
            chaSeqs = []
            i += 1
            setCharPos(i)  # 重置状态
            i += 1

        for id in chaIds:
            cha = character_dict[id]
            act = cha.actions.get(i)
            if act is not None:
                chaSeqs.append(cha)
                if len(cha.currentActions) == 0:
                    cha.currentActions.append(cha.lastAction)
                cha.currentActions.append(act)
                cha.lastAction = act

        i += 1
    steps.append(['STAGE'])
    return steps


result_file = open('out.txt', 'w')
result_file.write('# time %s\n' % datetime.datetime.now())
ghl_list = ['_cy', '_am', '_mks', '_jfw', '_nbe', '_lfl', '_kln', '_lyd']
for fid in ghl_list:
    if isinstance(fid, int):
        layaf = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'FeLaya/laya/pages/group_04/FeStage%02d.ui' % fid)
        varname = 'chap%02d' % fid
    else:
        layaf = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'FeLaya/laya/pages/ghb/FeStage%s.ui' % fid)
        varname = 'chap%s' % fid
    if os.path.isfile(layaf):  # and (fid == 1 or fid == 3)
        steps = parse_file(layaf)
        print 'steps:', layaf
        result_file.write('%s = [\n' % varname)
        result_file.write('## %s\n' % layaf)
        for i in steps:
            if i is None:
                continue
            print i
            result_file.write('%s' % i)
            result_file.write(',\n')
        result_file.write(']\n')
    else:
        print layaf, 'not existed'

result_file.close()
