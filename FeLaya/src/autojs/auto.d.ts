function click(x: number, y: number);

function gesture(duration: number, ...points);

function sleep(ms: number);

function toast(msg: string);

function exit();

interface Point {
    x: number;
    y: number;
}
//app
interface Intent {
    action: string;//android.intent.action.
    packageName: string;
    className: string;
}
namespace app {
    function launch(packageName: string);
    function launchPackage(packageName: string);
    function currentPackage(): string;
    function startActivity(name: string)
    function intent(options: Intent);
}
namespace engines {
    function myEngine();
}

//images
type Color = number

class Image {
    pixel(x: number, y: number): Color
}

function requestScreenCapture(): boolean;

function captureScreen(): Image;

class colors {
    /**
     *
     * @param alpha
     * @param red
     * @param green
     * @param blue
     */
    static argb(alpha, red, green, blue);

    /**
     *
     * @param color1
     * @param color2
     * @param threshold  颜色相似度临界值，默认为4。取值范围为0~255。这个值越大表示允许的相似程度越小，如果这个值为0，则两个颜色相等时该函数才会返回true。
     * @param algorithm
     */
    static isSimilar(color1: Color, color2: Color, threshold?: number, algorithm?): boolean;
    static toString(color: Color): string;
}
class device {
    static width: number;
    static height: number;
}
namespace ui {
    function run(cb: Function);//Android的runOnUiThread
}
//悬浮窗
class FloatyWindow {

}
namespace floaty {
    function window(layout: string): FloatyWindow;
    function closeAll();
}