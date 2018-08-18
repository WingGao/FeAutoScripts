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

function initEnv() {
    toast(device.width + 'x' + device.height)
    if (device.height >= 2040) {
        FE_DY = 72 / 2
    } else {
        FE_DY = (device.height - 2160) / 2
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
    let c = img.pixel(280, 1985 + FE_DY)
    if (colors.isSimilar(c, colors.argb(-1, 169, 61, 85))) {
        return FeState.MY_TURN
    } else if (colors.isSimilar(img.pixel(143, 350 + FE_DY), colors.argb(-1, 0, 132, 193))) {
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

let MFW = floaty.window(
    <horizontal>
        <text id="feText" textSize="16sp" textColor="#f44336" text="info" w="auto" />
        <button id="feExit" text="停" />
    </horizontal>
)
MFW.feExit.click(function () {
    exit()
})

function updateInfo(msg) {
    ui.run(() => MFW.feText.setText(msg))
}

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
        sleep(1000)
    }
}

function test() {
    toast(feState())
}

initEnv()
check_app()
loop_dyz(FeLeve.LUNATIC)