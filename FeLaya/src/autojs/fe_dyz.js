setTimeout(() => {
    // check_app()
    // loop_dyz(FeLeve.LUNATIC)
    // showFeInfo()
    loop_enemyturn()
}, 200)
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
const P_SAFE = { x: 1050, y: 180 } //安全点
const P_TEAM = { x: 175, y: 420, color: '#00669c' } //小队
const P_TURN = { x: 260, y: 2045, color: '#db86a4' } //危险范围

function initEnv() {
    toast(device.width + 'x' + device.height)
    if (device.height >= 2040) {
        // FE_DY = 72 / 2
    } else {
        FE_DY = (device.height - 2160) / 2
    }
}
/**
 * 点击，自动计算偏移
 * @param {number|Point} xOrPoint 
 * @param {number} y 
 */
function wclick(xOrPoint, y) {
    if (typeof xOrPoint == "number") {
        click(x, y + FE_DY)
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
    for (let i = 0; i < steps.length; i++) {
        let step = steps[i];
        let cmd = step[0]
        switch (cmd) {
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
                sleep(1000)
                click(299, 1062 + FE_DY)// 点击 设置
                sleep(1000)
                while (true) {
                    click(1045, 1870 + FE_DY)// 有时候已经stage了
                    sleep(1000)
                    if ([FeState.MY_TURN, FeState.CHAPTER].indexOf(feState()) >= 0) {
                        break
                    }
                }

        }
    }
}

function feState(check_btn) {
    let img = captureScreen();
    if (colors.isSimilar(getColor(img, P_TURN), P_TURN.color)) {
        return FeState.MY_TURN
    } else if (colors.isSimilar(getColor(img, P_TEAM), P_TEAM.color)) {
        return FeState.CHAPTER
    }
    return FeState.UNKNOWN
}
function wait_state(state_or_list, check_btn) {
    while (true) {
        let state = feState(check_btn)
        if (typeof state_or_list == 'array' && state_or_list.indexOf(state) >= 0) {
            break
        } else if (state_or_list == state) {
            break
        }
        sleep(2000)
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
            <text id="pTeam" textSize="16sp" textColor="white" text="pTeam" w="100" />
            <text id="pTurn" textSize="16sp" textColor="white" text="pTurn" w="100" />
        </vertical>
    )
    let img = captureScreen();
    ui.run(() => {
        window.pSafe.setBackgroundColor(img.pixel(P_SAFE.x, P_SAFE.y + FE_DY))
        let colorTeam = img.pixel(P_TEAM.x, P_TEAM.y + FE_DY)
        window.pTeam.setBackgroundColor(colorTeam)
        logInfo += "P_TEAM " + colors.toString(colorTeam) + "\n"
        let colorTurn = getColor(img, P_TURN)
        window.pTurn.setBackgroundColor(colorTurn)
        logInfo += "P_TURN " + colors.toString(colorTurn) + "\n"
    })

    logInfo += "feState " + feState()
    console.log("\n" + logInfo)

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
        wait_state(FeState.MY_TURN)
        startFe([['AUTO'], ['END']])
        wait_state(FeState.CHAPTER, true)
        click(310, 1825 + FE_DY) //点击 确定
        sleep(2000)
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

const chap_dyz = [
    ['D', (341, 1693), (331, 1429)],
    ['D', (200, 1686), (210, 1432)],
    ['END'],
    ['T', (331, 1429), (751, 1429), (616, 1424), (741, 1559), (756, 1429), (751, 1569), (876, 1694)],
    ['D', (210, 1432), (614, 1427)],
    ['D', (203, 1830), (880, 1690)],
    ['D', (198, 1555), (880, 1697)],
    ['END'],
    ['STAGE'],
]

function test() {
    toast(feState())
}

initEnv()
