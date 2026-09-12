import time
import lirc 
from gpiozero import RGBLED

rgb_Lv = [100, 10, 0]
rgb_color = [00, 00, 00]

led = RGBLED(18, 19, 20)
makerobo_blocking = 0

def makerobo_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def makerobo_ledColorSet(color):
    r_val = 100 - color[0]
    g_val = 100 - color[1]
    b_val = 100 - color[2]
    r_val = makerobo_map(r_val, 0, 100, 0, 1)
    g_val = makerobo_map(g_val, 0, 100, 0, 1)
    b_val = makerobo_map(b_val, 0, 100, 0, 1)
    led.color = (r_val, g_val, b_val)


def makerobo_setup():
    global lirc_client
    lirc_client = lirc.Client()  # 创建 LIRC 客户端


def RGB_control(config):
    global color
    if config == "KEY_CHANNELDOWN":
        rgb_color[0] = rgb_Lv[0]
        print("makerobo Red OFF")

    if config == "KEY_CHANEL":
        rgb_color[0] = rgb_Lv[1]
        print("makerobo Light Red")

    if config == "KEY_CHANNELUP":
        rgb_color[0] = rgb_Lv[2]
        print("makerobo Red")

    if config == "KEY_PREVIOUS":
        rgb_color[1] = rgb_Lv[0]
        print("makerobo Green OFF")

    if config == "KEY_NEXT":
        rgb_color[1] = rgb_Lv[1]
        print("makerobo Light Green")

    if config == "KEY_PLAYPAUSE":
        rgb_color[1] = rgb_Lv[2]
        print("makerobo Green")

    if config == "KEY_VOLUMEDOWN":
        rgb_color[2] = rgb_Lv[0]
        print("makerobo Blue OFF")

    if config == "KEY_VOLUMEUP":
        rgb_color[2] = rgb_Lv[2]
        print("makerobo Light Blue")

    if config == "KEY_EQUAL":
        rgb_color[2] = rgb_Lv[2]
        print("makerobo Blue")

def makerobo_loop():
    global lirc_client
    while True:
        try:
            code = lirc_client.readline(.1)  # 超时设置为 0.1 秒
            if code:
                print("Command:", code.strip())
                RGB_control(code.strip())
                makerobo_ledColorSet(rgb_color)
        except BlockingIOError:
            pass
        except Exception as e:
            print(f"Error: {e}")

def destroy():
    global lirc_client
    led.close()
    lirc_client.close()  # 关闭 LIRC 客户端


if __name__ == "__main__":
    try:
        makerobo_setup()
        makerobo_loop()
    except KeyboardInterrupt:
        destroy()
