setTimeout(() => {
    // check_app()
    showInfoView()
    // loop_dyz(FeLeve.INFERNAL)
    // showFeInfo()
    // loop_fe(chap_km_j) //周二卡谬练级
    // loop_fe(chap_ll_j) //周三罗罗练级
    // loop_fe(chap_wed) //周六瓦尔达练级
    loop_fe(chap_aews) // 周日-阿尔维斯

    // startFe(chap_km)
    // loop_enemyturn()
    // loop_auto(2)
}, 5000)
// setInterval(() => {
//     exit()
// }, 3000)

let FE_DY = 0 //偏移
const FE_PACKAGE_NAME = "com.nintendo.zaba"
const FE_ACTIVITY_NAME = "org.cocos2dx.cpp.AppActivity"
const FeState = {
    MY_TURN: 1,
    ENEMY_TURN: 2,
    CHAIN_10: 3,// 10连界面
    CHAPTER: 4, //章节页面
    UNKNOWN: 100
}
const FeLeve = {
    NORMAL: 0,
    HARD: 1,
    LUNATIC: 2,
    INFERNAL: 3,
}
const P_SAFE = { x: 1070, y: 1920 } //安全点
const P_BACK = { x: 40, y: 545, color: '#fbcdc2' } //章节页返回
const P_TEAM = { x: 175, y: 420, color: '#00669c' } //小队
const P_TURN = { x: 260, y: 2045, color: '#db86a4' } //危险范围
const P_SKIP = { x: 800, y: 220, color: '#482128' } //跳过
const P_ERR_1 = { x: 320, y: 1130, color: '#6aa181' } //错误1 803-3101

function initEnv() {

    if (device.height >= 2040) {
        // FE_DY = 72 / 2
    } else {
        FE_DY = (device.height - (2160 - 72)) / 2 - 72
    }
    toast(device.width + 'x' + device.height + ', dy=' + FE_DY)
}
/**
 * 点击，自动计算偏移
 * @param {number|Point} xOrPoint 
 * @param {number} y 
 */
function wclick(xOrPoint, y) {
    if (typeof xOrPoint == "number") {
        click(xOrPoint, y + FE_DY)
    } else if (typeof xOrPoint == "object" && typeof xOrPoint.x == "number") {
        click(xOrPoint.x, xOrPoint.y + FE_DY)
    }
}
/**
 * 获取颜色，自动计算偏移
 * @param {Image} img
 * @param {number|Point} xOrPoint 
 * @param {number} y 
 * @returns {Color}
 */
function getColor(img, xOrPoint, y) {
    if (typeof xOrPoint == "number") {
        return img.pixel(xOrPoint, y + FE_DY)
    } else if (typeof xOrPoint == "object" && typeof xOrPoint.x == "number") {
        return img.pixel(xOrPoint.x, xOrPoint.y + FE_DY)
    }
}

function startFe(steps, can_exit) {
    const get_fix_point = (p) => {
        return [p[0], p[1] + FE_DY]
    }
    for (let i = 0; i < steps.length; i++) {
        let step = steps[i];
        let cmd = step[0]
        console.log('step:', step)
        switch (cmd) {
            case "D":
                gesture(500, get_fix_point(step[1]), get_fix_point(step[2]))
                sleep(700)
                // gesture(500, [[step[1], step[2] + FE_DY], [step[3], step[4] + FE_DY]])
                break
            case "T":
                gesture(500, get_fix_point(step[1]), get_fix_point(step[2]), get_fix_point(step[3]))
                sleep(700)
                break
            case "RESTART": //重新挑战
                wait_state(FeState.MY_TURN, true)
                click(120, 1975 + FE_DY)// 点击 设置
                sleep(500)
                click(300, 1330 + FE_DY)
                sleep(500)
                click(300, 1100 + FE_DY)// 点击 确定
                sleep(5000)
                break
            case "AUTO":
                click(120, 1975 + FE_DY)// 点击 设置
                sleep(500)
                click(300, 1250 + FE_DY)// 点击 自动
                sleep(500)
                click(300, 1100 + FE_DY)// 点击 确定
                sleep(5000)
                break
            case "END":
                click(515, 1945 + FE_DY)// 点击 设置
                sleep(500)
                click(299, 1062 + FE_DY)// 点击 设置
                sleep(500)
                while (true) {
                    click(1045, 1870 + FE_DY)// 有时候已经stage了
                    sleep(1000)
                    if ([FeState.MY_TURN, FeState.CHAPTER].indexOf(feState(true)) >= 0) {
                        break
                    }
                }
                break
            case "WAIT":
                wait_state(step[1], true)
                break

        }
    }
}

function feState(check_btn) {
    let img = captureScreen();
    let state = FeState.UNKNOWN
    if (colors.isSimilar(getColor(img, P_TURN), P_TURN.color)) {
        state = FeState.MY_TURN
    } else if (colors.isSimilar(getColor(img, P_BACK), P_BACK.color)) {
        state = FeState.CHAPTER
    }
    if (check_btn) {
        let pts = [P_SKIP, P_ERR_1]
        pts.forEach(pt => {
            if (colors.isSimilar(getColor(img, pt), pt.color)) {
                wclick(pt);
            }
        })
        wclick(P_SAFE)
    }
    //检查确认按钮
    let check_ok = true
    if (check_ok && check_btn) {
        // let okPos = images.findMultiColors(img, '#456050', [
        //     [0, 10, '#445b4b'],
        //     [0, 20, '#3b5645'],
        //     [0, 30, '#336044'],
        //     [0, 40, '#2e6f48'],
        // ], { region: [350, 510 + FE_DY, 1, img.getHeight() - (510 + FE_DY)], threshold: 10 })
        let okPos = images.findColor(img, '#456050', { region: [350, 510 + FE_DY, 1, img.getHeight() - (510 + FE_DY)] })
        if (okPos != null) {
            console.log('find ok btn ', okPos)
            wclick(okPos.x, okPos.y + 10)
        }
    }
    console.log('feState', state)
    return state
}
function wait_state(state_or_list, check_btn) {
    while (true) {
        let state = feState(check_btn)
        if (typeof state_or_list == 'array' && state_or_list.indexOf(state) >= 0) {
            break
        } else if (state_or_list == state) {
            break
        }
        sleep(1000)
    }
}
function hexToARGB(hex) {
    let a = hex >> 24 & 0xFF;
    var r = hex >> 16 & 0xFF;
    var g = hex >> 8 & 0xFF;
    var b = hex & 0xFF;
    return [a, r, g, b];
}
//显示主题定位信息
function showFeInfo() {
    // canvas https://github.com/hyb1996/Auto.js/blob/dev/autojs/src/main/java/com/stardust/autojs/core/graphics/ScriptCanvas.java
    var redImg = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGElEQVQYlWP8z8Dwn4EIwESMolGF1FMIAD2cAhL1w47oAAAAAElFTkSuQmCC'
    let logInfo = ""
    let window = floaty.window(
        <vertical padding="5">
            <text id="pSafe" textSize="16sp" textColor="white" text="pSafe" w="100" />
            <text id="pBack" textSize="16sp" textColor="white" text="pBack" w="100" />
            <text id="pTeam" textSize="16sp" textColor="white" text="pTeam" w="100" />
            <text id="pTurn" textSize="16sp" textColor="white" text="pTurn" w="100" />
            <text id="pSkip" textSize="16sp" textColor="white" text="pSkip" w="100" />
            <text id="pErr1" textSize="16sp" textColor="white" text="pErr1" w="100" />
        </vertical>
    )
    let img = captureScreen();
    ui.run(() => {
        window.pSafe.setBackgroundColor(img.pixel(P_SAFE.x, P_SAFE.y + FE_DY))
        let colorBack = img.pixel(P_BACK.x, P_BACK.y + FE_DY)
        window.pBack.setBackgroundColor(colorBack)
        logInfo += "P_BACK " + colors.toString(colorBack) + "\n"
        let colorTeam = img.pixel(P_TEAM.x, P_TEAM.y + FE_DY)
        window.pTeam.setBackgroundColor(colorTeam)
        logInfo += "P_TEAM " + colors.toString(colorTeam) + "\n"
        let colorTurn = getColor(img, P_TURN)
        window.pTurn.setBackgroundColor(colorTurn)
        logInfo += "P_TURN " + colors.toString(colorTurn) + "\n"
        let colorSkip = getColor(img, P_SKIP)
        window.pSkip.setBackgroundColor(colorSkip)
        logInfo += "P_SKIP " + colors.toString(colorSkip) + "\n"

        let colorErr1 = getColor(img, P_ERR_1)
        window.pErr1.setBackgroundColor(colorErr1)
        logInfo += "P_ERR_1 " + colors.toString(colorErr1) + "\n"
    })
    //ok按钮
    let okX = 361, okY = 1782
    for (let i = 0; i < 50; i++) {
        let col = getColor(img, okX, okY + i)
        logInfo += 'ok_' + i + ' ' + colors.toString(col) + "\n"
    }

    logInfo += "feState " + feState(false)
    console.log("\n" + logInfo)
    sleep(5000)
}

function check_app() {
    setInterval(function () {
        let cp = currentPackage();
        console.log('currentPackage', cp)
        // toast(currentPackage())
        if (cp != FE_PACKAGE_NAME) {
            toast("非fe窗口，停止脚本")
            exit()
        }
    }, 1000)
}
if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
}

app.intent({
    action: "VIEW",
    packageName: FE_PACKAGE_NAME,
    className: FE_ACTIVITY_NAME,
})

// 信息窗口
let MFW;
function showInfoView() {
    if (MFW != null) return;
    MFW = floaty.window(
        <horizontal>
            <text id="feText" textSize="16sp" textColor="#f44336" text="info" w="auto" />
            <button id="feExit" text="停" />
        </horizontal>
    )
    MFW.feExit.click(function () {
        exit()
    })
}

function updateInfo(msg) {
    ui.run(() => MFW.feText.setText(msg))
}
// 大压制
function loop_dyz(level) {
    let cnt = 0;
    while (true) {
        cnt += 1
        updateInfo("dyz round " + cnt)
        // 地狱
        if (level == FeLeve.INFERNAL) {
            click(310, 735 + FE_DY)
        } else if (level == FeLeve.LUNATIC) {
            click(320, 1065 + FE_DY)
        } else {
            toast("no such level")
            return exit()
        }
        sleep(2000)
        click(310, 1630 + FE_DY)
        sleep(1000)
        wait_state(FeState.MY_TURN, true)
        let steps = [
            ['D', [199, 1687], [205, 1426]],
            ['D', [346, 1689], [202, 1421]],
            ['D', [205, 1426], [202, 1155]],
            ['AUTO'], ['END']
        ]
        startFe(steps)
        wait_state(FeState.CHAPTER, true)
        click(310, 1825 + FE_DY) //点击 确定
        sleep(2000)
    }
}
/**
 * 自动任务
 * 比如，旋涡30级,自动
 * @param {number} chapterIdx 章节的位置，重上往下，0开始
 */
function loop_auto(chapterIdx) {
    let chapPoints = {
        2: { x: 275, y: 1455 },
    }

    showInfoView()
    let cnt = 0;
    let chapPt = chapPoints[chapterIdx]
    if (chapPt == null) {
        alert('当前章节不存在')
        return
    }
    while (true) {
        cnt += 1
        updateInfo("fe_auto round " + cnt)
        wclick(chapPt)
        wait_state(FeState.MY_TURN, true)
        let steps = [
            ['AUTO'],
            ['END']
        ]
        startFe(steps)
        wait_state(FeState.CHAPTER, true)
    }
}
function loop_fe(steps) {
    showInfoView()
    let cnt = 0;
    while (true) {
        cnt += 1
        updateInfo("fe round " + cnt)
        wait_state(FeState.MY_TURN, true)
        startFe(steps)
    }
}
// 自动加速敌人回合
function loop_enemyturn() {
    showInfoView()
    while (true) {
        updateInfo("waiting enemy")
        wait_state(FeState.UNKNOWN)
        sleep(2000)
        if (feState() == FeState.UNKNOWN) {
            updateInfo("clicking")
            let cnt = 0
            while (true) {
                cnt++;
                if (cnt % 10 == 0 && feState() == FeState.MY_TURN) {
                    break;
                } else {
                    wclick(P_SAFE)
                    sleep(200)
                }
            }
        }
    }
}
// #region 练级步骤
// 卡谬练级-远程
const chap_km_y = [
    ['D', [456, 1803], [451, 1438]],
    ['D', [807, 1804], [452, 1799]],
    ['END'],
    ['T', [268, 1804], [273, 1444], [443, 1259]],
    ['D', [629, 1803], [449, 1258]],
    ['WAIT', FeState.MY_TURN],
    ['RESTART'],
]
// 卡谬练级-近战
const chap_km_j = [
    ['D', [456, 1803], [451, 1438]],
    ['D', [807, 1804], [452, 1799]],
    ['END'],
    ['T', [268, 1804], [273, 1444], [443, 1259]],
    ['D', [451, 1438], [626, 1798]],
    ['D', [631, 1621], [449, 1258]],
    ['WAIT', FeState.MY_TURN],
    ['RESTART'],
]
// 罗罗-近战
const chap_ll_j = [
    ['D', [451, 1626], [85, 1630]],
    ['D', [452, 1808], [89, 1808]],
    ['D', [637, 1619], [269, 1631]],
    ['END'],
    ['D', [269, 1631], [85, 1448]],
    ['D', [85, 1630], [269, 1806]],
    ['D', [631, 1803], [271, 1807]], //治疗
    ['WAIT', FeState.MY_TURN],
    ['D', [89, 1808], [77, 1443]],
    ['RESTART'],
]
// 罗罗-远程
const chap_ll_y = [
    ['D', [451, 1626], [85, 1630]],
    ['D', [452, 1808], [89, 1808]],
    ['D', [637, 1619], [269, 1631]],
    ['END'],
    ['D', [269, 1631], [85, 1448]],
    // ['D', [85, 1630], [269, 1806]],
    ['D', [89, 1808], [77, 1443]],
    ['RESTART'],
]
// 周六-瓦尔达
const chap_wed = [
    ['D', [630, 899], [450, 1083]],
    ['END'],
    ['D', [453, 897], [453, 1262]],
    ['D', [267, 1082], [450, 1271]],
    ['WAIT', FeState.MY_TURN], //等待升级
    // ['D', [450, 1083], [90, 1083]],
    // ['D', [271, 897], [88, 1085]], //治疗
    ['RESTART'],
]
// 周日-阿尔维斯
const chap_aews = [
    ['T', [453, 897], [465, 1262], [817, 1262]],
    ['D', [634, 896], [819, 1258]],
    ['WAIT', FeState.MY_TURN], //等待升级
    ['RESTART'],
]
// #endregion

function test() {
    toast(feState())
}

initEnv()
